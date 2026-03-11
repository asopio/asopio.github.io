---
layout: default
title: "Alex Sopio"
---

<section class="hero">
  <h1 class="hero-title">Alex Sopio</h1>
  <p class="hero-subtitle">Physicist &amp; AI Scientist</p>
  <p class="hero-affiliation">// high-energy physics · machine learning · algorithmic trading</p>
  <div class="hero-links">
    <a class="btn btn-primary" href="https://github.com/asopio" target="_blank" rel="noopener noreferrer">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
      GitHub
    </a>
    <a class="btn btn-secondary" href="/publications/">Publications</a>
    <a class="btn btn-secondary" href="/talks/">Talks</a>
    <a class="btn btn-secondary" href="/research/">Research</a>
  </div>
</section>

<div class="container">

  <section class="section">
    <h2 class="section-title"><span class="dot"></span>About</h2>
    <div class="content-container" style="padding:0">
      <p>
        I am a physicist and AI scientist with a background in high-energy particle physics and a passion for applying machine learning to complex, data-rich problems. My research spans jet physics at the ATLAS experiment, graph neural networks, and quantitative finance.
      </p>
      <p>
        I enjoy building tools at the intersection of physics intuition and modern deep-learning architectures — from LundNet jet taggers to GNNs in Julia. When not crunching collider data, I explore algorithmic trading strategies and write about things I find interesting.
      </p>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title"><span class="dot"></span>Recent Posts</h2>
    <div class="post-list">
      {% for post in site.posts limit:5 %}
      <a class="post-item" href="{{ post.url }}">
        <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span>
        <span class="post-title">{{ post.title }}</span>
      </a>
      {% endfor %}
    </div>
    {% if site.posts.size > 5 %}
    <p style="margin-top:1.2rem; font-size:.88rem;">
      <a href="/blog/">View all posts →</a>
    </p>
    {% endif %}
  </section>

  <section class="section">
    <h2 class="section-title"><span class="dot"></span>Highlights</h2>
    <div class="card-grid">
      <div class="card">
        <div class="card-title">LundNet Jet Tagger</div>
        <div class="card-meta">ATLAS · Graph Neural Networks</div>
        <p class="card-desc">Developed a GNN-based jet tagger using the Lund plane representation, implemented in both PyTorch and Julia's Flux.jl.</p>
        <div class="tag-list">
          <span class="tag">Python</span>
          <span class="tag">Julia</span>
          <span class="tag">GNN</span>
          <span class="tag">HEP</span>
        </div>
      </div>
      <div class="card">
        <div class="card-title">IMC Prosperity Challenge</div>
        <div class="card-meta">Algorithmic Trading · Top 37 / 1000+</div>
        <p class="card-desc">Designed and implemented automated trading strategies for the IMC Prosperity challenge, finishing in the top 4%.</p>
        <div class="tag-list">
          <span class="tag">Python</span>
          <span class="tag">Quant</span>
          <span class="tag">Trading</span>
        </div>
      </div>
      <div class="card">
        <div class="card-title">GNNs with Julia</div>
        <div class="card-meta">Flux.jl · Particle Physics</div>
        <p class="card-desc">Graph Neural Networks in Julia using Flux.jl, with jet construction via Python bindings to FastJet.</p>
        <div class="tag-list">
          <span class="tag">Julia</span>
          <span class="tag">Flux.jl</span>
          <span class="tag">FastJet</span>
        </div>
      </div>
    </div>
  </section>

</div>

