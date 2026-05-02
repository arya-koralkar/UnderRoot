"use client";
import React, { useState } from 'react';
import { Mail, Lock, ArrowLeft, User, Library, GraduationCap, ChevronDown } from 'lucide-react';

export default function SignInPage() {
  const [credentials, setCredentials] = useState({
    fullName: '',
    email: '',
    password: '',
    role: 'Student',
    department: ''
  });
  const [authBtnHover, setAuthBtnHover] = useState(false);

  const theme = {
    bg: '#FCFBF7',
    text: '#1A2F23',
    cardBg: '#ffffff',
    cardBorder: '#E5E1D5',
    logoBg: '#1A2F23',
    btnBg: '#1A2F23',
    btnHoverBg: '#2D4D3A',
    btnText: '#FCFBF7',
    borderLight: 'rgba(26,47,35,0.1)',
  };

  const inputStyle: React.CSSProperties = {
    width: '100%',
    background: 'transparent',
    border: `1px solid ${theme.borderLight}`,
    borderRadius: 3,
    padding: '12px 12px 12px 38px',
    fontSize: 14,
    color: theme.text,
    outline: 'none',
    fontFamily: "'Playfair Display', serif",
    boxSizing: 'border-box',
  };

  const labelStyle: React.CSSProperties = {
    fontSize: 9,
    fontWeight: 700,
    textTransform: 'uppercase',
    letterSpacing: '0.2em',
    opacity: 0.5,
    display: 'block',
    marginBottom: 6,
    color: theme.text,
    fontFamily: 'Inter, sans-serif',
  };

  const handleSignIn = (e: React.FormEvent) => {
    e.preventDefault();
    if (credentials.email && credentials.fullName) {
      window.location.href = '/scriptorium';
    }
  };

  return (
    <div
      suppressHydrationWarning
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 24,
        background: theme.bg,
        color: theme.text,
        fontFamily: 'Inter, sans-serif',
        position: 'relative',
      }}
    >
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Inter:wght@400;600;700&display=swap');
        * { box-sizing: border-box; }
      `}</style>

      <a
        href="/"
        style={{
          position: 'absolute', top: 28, left: 28,
          fontSize: 10, fontWeight: 700,
          textTransform: 'uppercase', letterSpacing: '0.15em',
          opacity: 0.5, color: theme.text,
          textDecoration: 'none',
          display: 'flex', alignItems: 'center', gap: 6,
          fontFamily: 'Inter, sans-serif',
        }}
        onMouseEnter={e => (e.currentTarget.style.opacity = '1')}
        onMouseLeave={e => (e.currentTarget.style.opacity = '0.5')}
      >
        <ArrowLeft size={14} /> Back to Home
      </a>

      <div style={{
        background: theme.cardBg,
        border: `1px solid ${theme.cardBorder}`,
        borderRadius: 8,
        padding: 48,
        width: '100%',
        maxWidth: 440,
        boxShadow: '0 4px 24px rgba(0,0,0,0.07)',
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginBottom: 36, gap: 10 }}>
          <div style={{
            width: 48, height: 48, background: theme.logoBg, borderRadius: 4,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: "'Playfair Display', serif", fontSize: 22, fontWeight: 700,
            color: '#fff', boxShadow: '0 2px 10px rgba(0,0,0,0.15)',
          }}>U</div>
          <h2 style={{
            fontFamily: "'Playfair Display', serif", fontWeight: 900,
            fontSize: 30, textTransform: 'uppercase', letterSpacing: '-0.02em',
            color: theme.text, margin: 0,
          }}>Sign In</h2>
          <p style={{
            fontFamily: "'Playfair Display', serif", fontStyle: 'italic',
            fontSize: 13, opacity: 0.55, textAlign: 'center', color: theme.text, margin: 0,
          }}>
            Enter your institutional credentials to enter the library.
          </p>
        </div>

        <form onSubmit={handleSignIn} style={{ display: 'flex', flexDirection: 'column', gap: 20 }} suppressHydrationWarning>

          {/* Scholarly Role */}
          <div suppressHydrationWarning>
            <label style={labelStyle}>Scholarly Role</label>
            <div style={{ position: 'relative' }} suppressHydrationWarning>
              <GraduationCap style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', opacity: 0.3, color: theme.text }} size={14} />
              <select
                suppressHydrationWarning
                value={credentials.role}
                onChange={e => setCredentials(prev => ({ ...prev, role: e.target.value }))}
                style={{ ...inputStyle, appearance: 'none', cursor: 'pointer' }}
              >
                <option value="Student">Student</option>
                <option value="Faculty">Faculty Member</option>
                <option value="Researcher">Independent Researcher</option>
                <option value="Administrator">Institutional Administrator</option>
              </select>
              <ChevronDown style={{ position: 'absolute', right: 12, top: '50%', transform: 'translateY(-50%)', opacity: 0.3, pointerEvents: 'none' }} size={14} />
            </div>
          </div>

          {/* Full Name */}
          <div suppressHydrationWarning>
            <label style={labelStyle}>Full Name</label>
            <div style={{ position: 'relative' }} suppressHydrationWarning>
              <User style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', opacity: 0.3, color: theme.text }} size={14} />
              <input
                suppressHydrationWarning
                required
                type="text"
                value={credentials.fullName}
                onChange={e => setCredentials(prev => ({ ...prev, fullName: e.target.value }))}
                style={inputStyle}
                placeholder="e.g., Julian Thorne"
              />
            </div>
          </div>

          {/* Email */}
          <div suppressHydrationWarning>
            <label style={labelStyle}>University Email</label>
            <div style={{ position: 'relative' }} suppressHydrationWarning>
              <Mail style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', opacity: 0.3, color: theme.text }} size={14} />
              <input
                suppressHydrationWarning
                required
                type="email"
                value={credentials.email}
                onChange={e => setCredentials(prev => ({ ...prev, email: e.target.value }))}
                style={inputStyle}
                placeholder="name@university.edu"
              />
            </div>
          </div>

          {/* Department */}
          <div suppressHydrationWarning>
            <label style={labelStyle}>
              {credentials.role === 'Student' ? 'Major / Program' : 'Department / Faculty'}
            </label>
            <div style={{ position: 'relative' }} suppressHydrationWarning>
              <Library style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', opacity: 0.3, color: theme.text }} size={14} />
              <input
                suppressHydrationWarning
                type="text"
                value={credentials.department}
                onChange={e => setCredentials(prev => ({ ...prev, department: e.target.value }))}
                style={inputStyle}
                placeholder={credentials.role === 'Student' ? 'e.g., Economics Major' : 'e.g., Dept. of Physics'}
              />
            </div>
          </div>

          {/* Password */}
          <div suppressHydrationWarning>
            <label style={labelStyle}>Password</label>
            <div style={{ position: 'relative' }} suppressHydrationWarning>
              <Lock style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', opacity: 0.3, color: theme.text }} size={14} />
              <input
                suppressHydrationWarning
                required
                type="password"
                value={credentials.password}
                onChange={e => setCredentials(prev => ({ ...prev, password: e.target.value }))}
                style={inputStyle}
                placeholder="••••••••"
              />
            </div>
          </div>

          <button
            type="submit"
            suppressHydrationWarning
            onMouseEnter={() => setAuthBtnHover(true)}
            onMouseLeave={() => setAuthBtnHover(false)}
            style={{
              width: '100%', marginTop: 4,
              background: authBtnHover ? theme.btnHoverBg : theme.btnBg,
              color: theme.btnText, border: 'none', borderRadius: 2,
              padding: '16px', fontSize: 10, fontWeight: 700,
              textTransform: 'uppercase', letterSpacing: '0.2em',
              cursor: 'pointer', transition: 'background 0.2s',
              boxShadow: '0 3px 12px rgba(0,0,0,0.15)',
              fontFamily: 'Inter, sans-serif',
            }}
          >
            Authenticate
          </button>
        </form>

        <div style={{
          marginTop: 28, paddingTop: 20,
          borderTop: `1px solid ${theme.borderLight}`,
          textAlign: 'center', fontSize: 9, fontWeight: 700,
          textTransform: 'uppercase', letterSpacing: '0.12em',
          opacity: 0.35, lineHeight: 1.8, color: theme.text,
          fontFamily: 'Inter, sans-serif',
        }}>
          Unauthorized access is strictly prohibited.<br />
          Contact faculty for account provisioning.
        </div>
      </div>
    </div>
  );
}