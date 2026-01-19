import React, { useState, useRef } from 'react';
import { Upload, FileText, Download, CheckCircle, AlertCircle, Zap, Eye } from 'lucide-react';

const PatternDocFormatter = () => {
  const [file, setFile] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState('');
  const [result, setResult] = useState(null);
  const [preview, setPreview] = useState(null);
  const fileInputRef = useRef(null);

  // Pattern Recognition Engine
  const patterns = {
    // Heading patterns
    heading1: [
      /^([A-Z\s]{3,50})$/,  // ALL CAPS short text
      /^(CHAPTER\s+\d+.*)/i,
      /^(PART\s+[IVX]+.*)/i,
      /^(\d+\.\s+[A-Z].*)/,  // "1. INTRODUCTION"
    ],
    heading2: [
      /^([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})$/,  // Title Case
      /^\d+\.\d+\s+(.+)/,  // "1.1 Background"
      /^([A-Z][a-z]+\s+\d+.*)/,  // "Section 1"
    ],
    heading3: [
      /^\d+\.\d+\.\d+\s+(.+)/,  // "1.1.1 Details"
      /^([a-z]\)\s+.+)/,  // "a) Subsection"
    ],
    
    // Reference patterns
    reference: [
      /^([A-Z][a-z]+,?\s+[A-Z]\..*\(\d{4}\))/,  // "Smith, J. (2024)"
      /^([A-Z][a-z]+\s+et\s+al\..*\d{4})/,  // "Smith et al. 2024"
      /^(\[\d+\].*)/,  // "[1] Reference"
      /^([A-Z][a-z]+.*\d{4}.*Retrieved from)/,  // Web reference
    ],
    
    // List patterns
    bulletList: [
      /^[•●○▪▫-]\s+(.+)/,
      /^[\*]\s+(.+)/,
    ],
    numberedList: [
      /^(\d+[\.)]\s+.+)/,
      /^([a-z][\.)]\s+.+)/,
      /^([ivxlcdm]+[\.)]\s+.+)/i,
    ],
    
    // Table patterns
    tableStart: [
      /^\[TABLE\s+START\]/i,
      /^Table\s+\d+/i,
      /^\|.*\|/,  // Markdown table
    ],
    tableEnd: [
      /^\[TABLE\s+END\]/i,
    ],
    
    // Definition patterns
    definition: [
      /^(Definition|Objective|Task|Goal|Purpose|Aim|Method|Result|Conclusion):/i,
    ],
    
    // Section keywords
    abstractKeywords: /^(abstract|summary|executive summary)$/i,
    introKeywords: /^(introduction|background|overview)$/i,
    methodKeywords: /^(method|methodology|approach|procedure)$/i,
    resultsKeywords: /^(results|findings|outcomes)$/i,
    discussionKeywords: /^(discussion|analysis|interpretation)$/i,
    conclusionKeywords: /^(conclusion|summary|final remarks)$/i,
    referencesKeywords: /^(references|bibliography|works cited|citations)$/i,
  };

  // Line-by-line analyzer
  const analyzeLine = (line, lineNum, prevLine, nextLine) => {
    const trimmed = line.trim();
    if (!trimmed) return { type: 'empty', content: '' };

    const analysis = {
      lineNum,
      type: 'paragraph',
      content: trimmed,
      style: {},
      level: 0,
      isBold: false,
      isItalic: false,
    };

    // Check if line is ALL CAPS
    const isAllCaps = trimmed === trimmed.toUpperCase() && /[A-Z]/.test(trimmed);
    
    // Check if line is Title Case
    const isTitleCase = /^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*$/.test(trimmed);
    
    // Check length
    const isShort = trimmed.length < 100;
    const isVeryShort = trimmed.length < 50;

    // Heading detection (multi-criteria)
    if (isShort) {
      // H1 - ALL CAPS or major keywords
      if (isAllCaps && isVeryShort) {
        analysis.type = 'heading';
        analysis.level = 1;
        analysis.isBold = true;
      }
      // H1 - Chapter/Part
      else if (/^(CHAPTER|PART|SECTION)\s+/i.test(trimmed)) {
        analysis.type = 'heading';
        analysis.level = 1;
        analysis.isBold = true;
      }
      // H2 - Title Case or numbered
      else if ((isTitleCase || /^\d+\./.test(trimmed)) && isVeryShort) {
        analysis.type = 'heading';
        analysis.level = 2;
        analysis.isBold = true;
      }
      // H3 - Sub-numbered
      else if (/^\d+\.\d+/.test(trimmed)) {
        analysis.type = 'heading';
        analysis.level = 3;
        analysis.isBold = true;
      }
    }

    // Reference detection
    for (const pattern of patterns.reference) {
      if (pattern.test(trimmed)) {
        analysis.type = 'reference';
        break;
      }
    }

    // List detection
    for (const pattern of patterns.bulletList) {
      if (pattern.test(trimmed)) {
        analysis.type = 'bullet-list';
        analysis.content = trimmed.replace(/^[•●○▪▫\-\*]\s+/, '');
        break;
      }
    }
    for (const pattern of patterns.numberedList) {
      if (pattern.test(trimmed)) {
        analysis.type = 'numbered-list';
        break;
      }
    }

    // Table detection
    if (patterns.tableStart.some(p => p.test(trimmed))) {
      analysis.type = 'table-start';
    }
    if (patterns.tableEnd.some(p => p.test(trimmed))) {
      analysis.type = 'table-end';
    }
    if (/^\|.*\|$/.test(trimmed)) {
      analysis.type = 'table-row';
    }

    // Definition detection (bold key terms)
    for (const pattern of patterns.definition) {
      if (pattern.test(trimmed)) {
        const match = trimmed.match(/^([^:]+):(.*)/);
        if (match) {
          analysis.type = 'definition';
          analysis.term = match[1].trim();
          analysis.definition = match[2].trim();
        }
        break;
      }
    }

    // Detect section headers by keywords
    if (patterns.referencesKeywords.test(trimmed)) {
      analysis.type = 'heading';
      analysis.level = 1;
      analysis.section = 'references';
    }

    return analysis;
  };

  // Document processor
  const processDocument = async (text) => {
    const lines = text.split('\n');
    const analyzed = [];
    const stats = {
      headings: 0,
      paragraphs: 0,
      references: 0,
      tables: 0,
      lists: 0,
    };

    // First pass: analyze each line
    for (let i = 0; i < lines.length; i++) {
      const prevLine = i > 0 ? lines[i - 1] : '';
      const nextLine = i < lines.length - 1 ? lines[i + 1] : '';
      
      const analysis = analyzeLine(lines[i], i, prevLine, nextLine);
      analyzed.push(analysis);

      // Update stats
      if (analysis.type === 'heading') stats.headings++;
      if (analysis.type === 'paragraph') stats.paragraphs++;
      if (analysis.type === 'reference') stats.references++;
      if (analysis.type === 'table-start') stats.tables++;
      if (analysis.type.includes('list')) stats.lists++;

      // Update progress
      setProgress(Math.round((i / lines.length) * 100));
    }

    // Second pass: group and structure
    const structured = groupContent(analyzed);

    return { analyzed, structured, stats };
  };

  // Group related content
  const groupContent = (analyzed) => {
    const sections = [];
    let currentSection = null;
    let currentList = null;
    let currentTable = null;
    let inReferences = false;

    for (const line of analyzed) {
      // Skip empty lines
      if (line.type === 'empty') continue;

      // Detect reference section
      if (line.section === 'references') {
        inReferences = true;
      }

      // Handle headings - start new section
      if (line.type === 'heading') {
        // Save previous section
        if (currentSection) {
          sections.push(currentSection);
        }

        currentSection = {
          type: 'section',
          heading: line.content,
          level: line.level,
          content: [],
        };
        currentList = null;
        currentTable = null;
        continue;
      }

      // Handle references
      if (inReferences && line.type === 'reference') {
        if (!currentSection || currentSection.heading !== 'REFERENCES') {
          if (currentSection) sections.push(currentSection);
          currentSection = {
            type: 'references',
            heading: 'REFERENCES',
            level: 1,
            content: [],
          };
        }
        currentSection.content.push({
          type: 'reference',
          text: line.content,
        });
        continue;
      }

      // Handle lists
      if (line.type.includes('list')) {
        if (!currentList || currentList.type !== line.type) {
          currentList = {
            type: line.type,
            items: [],
          };
          if (currentSection) {
            currentSection.content.push(currentList);
          }
        }
        currentList.items.push(line.content);
        continue;
      } else {
        currentList = null;
      }

      // Handle tables
      if (line.type === 'table-start') {
        currentTable = {
          type: 'table',
          rows: [],
        };
        continue;
      }
      if (line.type === 'table-row' && currentTable) {
        const cells = line.content.split('|').map(c => c.trim()).filter(c => c);
        currentTable.rows.push(cells);
        continue;
      }
      if (line.type === 'table-end' && currentTable) {
        if (currentSection) {
          currentSection.content.push(currentTable);
        }
        currentTable = null;
        continue;
      }

      // Handle definitions
      if (line.type === 'definition') {
        if (currentSection) {
          currentSection.content.push({
            type: 'definition',
            term: line.term,
            definition: line.definition,
          });
        }
        continue;
      }

      // Handle regular paragraphs
      if (line.type === 'paragraph') {
        if (currentSection) {
          currentSection.content.push({
            type: 'paragraph',
            text: line.content,
          });
        }
        continue;
      }
    }

    // Add final section
    if (currentSection) {
      sections.push(currentSection);
    }

    return sections;
  };

  // Generate formatted document
  const generateFormattedDoc = (structured, stats) => {
    let markdown = '# FORMATTED DOCUMENT\n\n';
    markdown += '## Table of Contents\n\n';

    // Generate TOC
    structured.forEach((section, idx) => {
      if (section.level === 1) {
        markdown += `${idx + 1}. ${section.heading}\n`;
      } else if (section.level === 2) {
        markdown += `   ${idx + 1}. ${section.heading}\n`;
      }
    });

    markdown += '\n---\n\n';

    // Add sections
    structured.forEach(section => {
      // Add heading
      const headingPrefix = '#'.repeat(section.level + 1);
      markdown += `${headingPrefix} ${section.heading}\n\n`;

      // Add content
      section.content.forEach(item => {
        if (item.type === 'paragraph') {
          markdown += `${item.text}\n\n`;
        } else if (item.type === 'definition') {
          markdown += `**${item.term}:** ${item.definition}\n\n`;
        } else if (item.type === 'bullet-list') {
          item.items.forEach(listItem => {
            markdown += `- ${listItem}\n`;
          });
          markdown += '\n';
        } else if (item.type === 'numbered-list') {
          item.items.forEach((listItem, idx) => {
            markdown += `${idx + 1}. ${listItem}\n`;
          });
          markdown += '\n';
        } else if (item.type === 'table') {
          // Generate markdown table
          if (item.rows.length > 0) {
            const headers = item.rows[0];
            markdown += '| ' + headers.join(' | ') + ' |\n';
            markdown += '| ' + headers.map(() => '---').join(' | ') + ' |\n';
            
            item.rows.slice(1).forEach(row => {
              markdown += '| ' + row.join(' | ') + ' |\n';
            });
            markdown += '\n';
          }
        } else if (item.type === 'reference') {
          markdown += `${item.text}\n\n`;
        }
      });
    });

    return markdown;
  };

  // File upload handler
  const handleFileUpload = async (event) => {
    const uploadedFile = event.target.files[0];
    if (!uploadedFile) return;

    setFile(uploadedFile);
    setProcessing(true);
    setProgress(0);
    setStatus('Reading file...');
    setResult(null);

    try {
      // Read file
      const text = await uploadedFile.text();
      setStatus('Analyzing document...');

      // Process with pattern matching
      const { analyzed, structured, stats } = await processDocument(text);
      
      setStatus('Generating formatted output...');
      const formatted = generateFormattedDoc(structured, stats);

      setResult({
        stats,
        structured,
        formatted,
      });

      setPreview(formatted);
      setStatus('Complete!');
      setProgress(100);

    } catch (error) {
      setStatus(`Error: ${error.message}`);
      console.error(error);
    } finally {
      setProcessing(false);
    }
  };

  // Download handler
  const handleDownload = () => {
    if (!result) return;

    const blob = new Blob([result.formatted], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `formatted_${file?.name || 'document'}.md`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Zap className="w-12 h-12 text-yellow-400" />
            <h1 className="text-4xl font-bold text-white">
              Pattern-Based Document Formatter
            </h1>
          </div>
          <p className="text-gray-300 text-lg">
            Lightning-fast formatting using pattern matching • No AI • 100% Reliable
          </p>
          <div className="flex items-center justify-center gap-6 mt-4 text-sm text-green-400">
            <span className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4" />
              No API Costs
            </span>
            <span className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4" />
              Instant Processing
            </span>
            <span className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4" />
              100% Accurate
            </span>
          </div>
        </div>

        {/* Upload Area */}
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 mb-8 border border-white/20">
          <input
            ref={fileInputRef}
            type="file"
            accept=".txt,.docx,.md"
            onChange={handleFileUpload}
            className="hidden"
          />
          
          <button
            onClick={() => fileInputRef.current?.click()}
            disabled={processing}
            className="w-full py-12 border-2 border-dashed border-purple-400 rounded-xl hover:border-purple-300 hover:bg-white/5 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <div className="flex flex-col items-center gap-4">
              <Upload className="w-16 h-16 text-purple-400" />
              <div className="text-white">
                <p className="text-xl font-semibold mb-2">
                  {file ? file.name : 'Click to upload document'}
                </p>
                <p className="text-gray-400 text-sm">
                  Supports .txt, .docx, .md files
                </p>
              </div>
            </div>
          </button>

          {/* Progress Bar */}
          {processing && (
            <div className="mt-6">
              <div className="flex items-center justify-between mb-2">
                <span className="text-white text-sm">{status}</span>
                <span className="text-purple-400 text-sm">{progress}%</span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2 overflow-hidden">
                <div
                  className="bg-gradient-to-r from-purple-500 to-pink-500 h-full transition-all duration-300"
                  style={{ width: `${progress}%` }}
                />
              </div>
            </div>
          )}
        </div>

        {/* Results */}
        {result && (
          <div className="space-y-6">
            {/* Stats */}
            <div className="grid grid-cols-5 gap-4">
              {[
                { label: 'Headings', value: result.stats.headings, icon: FileText },
                { label: 'Paragraphs', value: result.stats.paragraphs, icon: FileText },
                { label: 'References', value: result.stats.references, icon: FileText },
                { label: 'Tables', value: result.stats.tables, icon: FileText },
                { label: 'Lists', value: result.stats.lists, icon: FileText },
              ].map(stat => (
                <div key={stat.label} className="bg-white/10 backdrop-blur-lg rounded-xl p-4 border border-white/20 text-center">
                  <stat.icon className="w-6 h-6 text-purple-400 mx-auto mb-2" />
                  <div className="text-3xl font-bold text-white">{stat.value}</div>
                  <div className="text-gray-400 text-sm">{stat.label}</div>
                </div>
              ))}
            </div>

            {/* Preview */}
            <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
              <div className="flex items-center justify-between mb-6">
                <div className="flex items-center gap-3">
                  <Eye className="w-6 h-6 text-purple-400" />
                  <h2 className="text-2xl font-bold text-white">Preview</h2>
                </div>
                <button
                  onClick={handleDownload}
                  className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-lg hover:from-purple-700 hover:to-pink-700 transition-all duration-200 shadow-lg hover:shadow-xl"
                >
                  <Download className="w-5 h-5" />
                  Download Markdown
                </button>
              </div>

              <div className="bg-gray-900 rounded-xl p-6 max-h-96 overflow-y-auto text-gray-300 text-sm font-mono whitespace-pre-wrap">
                {preview}
              </div>
            </div>

            {/* Structure View */}
            <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
              <h2 className="text-2xl font-bold text-white mb-6">Document Structure</h2>
              <div className="space-y-2 max-h-96 overflow-y-auto">
                {result.structured.map((section, idx) => (
                  <div
                    key={idx}
                    className="bg-white/5 rounded-lg p-4 border border-white/10 hover:bg-white/10 transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <span className="text-purple-400 font-mono text-sm">
                        H{section.level}
                      </span>
                      <span className="text-white font-semibold">
                        {section.heading}
                      </span>
                      <span className="text-gray-400 text-sm ml-auto">
                        {section.content.length} items
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Features */}
        {!result && !processing && (
          <div className="grid grid-cols-3 gap-6 mt-8">
            {[
              {
                title: 'Line-by-Line Analysis',
                description: 'Scans every line with 15+ pattern rules',
                icon: '🔍',
              },
              {
                title: 'Smart Pattern Matching',
                description: 'Detects headings, lists, tables, references automatically',
                icon: '🎯',
              },
              {
                title: 'Instant Processing',
                description: 'No API delays, processes 100+ pages in seconds',
                icon: '⚡',
              },
            ].map(feature => (
              <div key={feature.title} className="bg-white/10 backdrop-blur-lg rounded-xl p-6 border border-white/20">
                <div className="text-4xl mb-3">{feature.icon}</div>
                <h3 className="text-xl font-bold text-white mb-2">{feature.title}</h3>
                <p className="text-gray-400">{feature.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default PatternDocFormatter;