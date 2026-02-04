---
name: a11y-base-web
description: Foundational accessibility patterns and requirements for AI-generated web code. This skill provides baseline rules for semantic HTML, ARIA usage, keyboard navigation, contrast, and inclusive language. Load this skill first before any accessibility analysis, remediation, or validation work. Other a11y skills (web-standards, a11y-remediator, a11y-validator, a11y-tester) build upon these fundamentals.
---

# Accessibility Fundamentals

Baseline accessibility patterns and requirements for technologies that render HTML and CSS.

### LLM Behavior and Tone Requirements
In addition to producing accessible code, GitHub Copilot and similar tools must also demonstrate respectful and bias-aware behavior in accessibility contexts. All generated output must follow these principles:

- **Respectful, Inclusive Language**
Use people-first language when referring to disabilities or accessibility needs (e.g., “person using a screen reader,” not “blind user”). Avoid stereotypes or assumptions about ability, cognition, or experience.

- **Bias-Aware and Error-Resistant**
Avoid generating content that reflects implicit bias or outdated patterns. Critically assess accessibility choices and flag uncertain implementations.

- **Verification-Oriented Responses**
When suggesting accessibility implementations or decisions, include reasoning or references to standards (e.g., WCAG, platform guidelines). If uncertainty exists, the assistant should state this clearly.

- **Clarity Without Oversimplification**
Provide concise but accurate explanations—avoid fluff, empty reassurance, or overconfidence when accessibility nuances are present.

- **Tone Matters**
Copilot output must be neutral, helpful, and respectful. Avoid patronizing language, euphemisms, or casual phrasing that downplays the impact of poor accessibility.

---

### Anti-Patterns and Mistakes to Avoid
- Using only placeholders to label inputs
- Suppressing visible focus with CSS resets or browser overrides
- Invalid ARIA usage on elements with semantic roles
- Invalid ARIA: Applying unsupported ARIA states to incorrect elements
- Don’t apply `role="button"` to a Button `<button>`
#### Bad Code example
```html 
<button role="button">Click me</button>
```
#### Good Code example
```html
<button>Click me</button>
```
- Don't apply role="link" to a Link <a>
#### Bad Code example
```html
<a role="link" href="#">Click me</a>
```
#### Good Code example
```html
<a href="#">Click me</a>
```
- Don't apply role="button" to a link <a>
#### Bad Code example
```html
<a role="button" href="#">Click me</a>      
```
#### Good Code example
```html
<a href="#">Click me</a>
```
- Don't apply role="link" to a Button <button>
#### Bad Code example
```html
<button role="link">Click me</button>   
```
#### Good Code example
```html
<button>Click me</button>
```
- Don't add aria-label to a button or link unless asked to
#### Bad Code example
```html
<button aria-label="Click me">Click me</button>
```
#### Good Code example
```html
<button>Click me</button>
- Avoid overuse of sectioning elements and ARIA landmarks
- Don't add any ARIA attributes unless asked to, rely on web standards first
- Using generic containers when semantic elements would be more appropriate
- Making entire large areas clickable when a specific element would suffice
- Separating interactive elements from their related content
- Breaking up natural content relationships with unnecessary containers

### Semantic Structure Best Practices

#### Content Organization
When presenting collections of similar items (like articles, cards, products):
1. Prefer list structures (`<ul>`, `<ol>`, `<li>`) over generic containers
2. Place headings within their related content containers, not as wrappers
3. Ensure the natural reading order matches the visual order
4. Keep interactive elements (links, buttons) close to their related content

#### Content Hierarchy
- Place the most important identifying content first within containers
- Group related content (e.g., image + heading + description) meaningfully
- Avoid unnecessary nesting levels
- Consider the logical order when content will be linearized

#### Interactive Elements
- Place interactive elements (links, buttons) on the most specific related content
- Avoid making large areas interactive when a smaller target would suffice
- Ensure the clickable area's purpose is clear from its immediate content
- Keep primary actions close to their related content

---

### Required Accessibility Patterns

#### Keyboard Navigation and Interaction
- All interactive elements must support full keyboard navigation using standard keys:
- Tab, Shift+Tab, Enter, Escape, Arrow keys
- Do not author custom focus styles - rely on native default browser focus rings 

#### Touch Targets
All interactive elements must meet a minimum touch target size of **24x24px** (or equivalent in `dp` or `pt`) to comply with WCAG 2.1. Larger sizing (such as 44x44px) is recommended for usability across Web, iOS, and Android but not a hard requirement.

Touch Target Requirements:
1. Required Minimum: 24x24px (WCAG 2.1 compliance)
2. Preferred Size: 44x44px (optimal usability)
3. Exception: When UI constraints make larger targets impossible, never go below 24x24px

#### Text Resize:
All content must support up to 200% text resizing:
- Use relative units like `em` and `rem`.

#### Buttons:
Use native button elements instead of fake button elements:
- Use `<button>` instead of `<div>` or `<span>` for clickables.

#### Label in Name:
Ensure the visible text label is included in the accessible name to support screen readers and voice control per WCAG 2.1 Success Criterion 2.5.3.
- Use `<label for="id">Visible Label</label>` or ensure `aria-label` includes the same visible text. Avoid using placeholder-only text for labeling. Use `aria-labelledby` when combining multiple text elements as the label.

#### 400% Zoom
Layouts must remain functional and readable at up to 400% zoom or scale:
- Support zoom with responsive grids and avoid horizontal scrolling.
- iOS/Android: Avoid fixed layouts that clip or overflow when scaling is increased.

#### Live Regions / Dynamic Updates
Auto-updating or dynamic content must be controllable and announced appropriately
- It may be up to the consumer of Arrow to manage dynamic updates
    - Web: Use ARIA live regions and visible controls (e.g., pause buttons).

#### Text Contrast
- Do not rely on color alone to convey meaning—include labels, icons, or visible states.
- Always show visible focus indicators on focusable elements. Use the default focus indicator.
- Text contrast must meet minimums:
    - 4.5:1 for normal text (defined as up to and including 18.5px regular or 14pt bold)
    - 3:1 for large text (≥18pt or ≥14pt bold)
    - 3:1 for non-text UI elements (e.g., icons, focus indicators, input borders, and buttons) against adjacent background

#### Non-text Contrast: 
Ensure non-text elements have sufficient color contrast.
- Non-text elements that are not decorative should meet a contrast ration minimum of 3:1

#### Text Alternatives
- Non-text elements (e.g., icons, images, SVGs) must provide meaningful alternatives or be marked as decorative. 
    - Before implementing any image-related accessibility:
        - Always explicitly ask whether an image is decorative or informative
        - Never assume an image needs alt text - this decision must come from the development team
        - Document the reasoning for treating an image as decorative or informative
    - Web: Use `alt`, `aria-label`, or `aria-labelledby`, or mark as decorative.
        - Informative image: 
            - Use `alt` for `<img>` e.g. `<img alt="some description">`
        - Use `aria-label` or `aria-labelledby` for non-image elements (e.g., SVGs, icons)
        - Decorative image:
            - Use empty/null `alt` value for `<img>` e.g. `<img alt="">`
            - Use `aria-hidden="true"` for non-image elements (e.g., SVGs, icons) that are purely decorative

#### Important Note on Content Decisions
The decision about whether an image is decorative or informative must be made by the development team. Copilot should not make assumptions about:
- Image purpose (decorative vs informative)
- Alt text content
- The need for additional ARIA labels on semantic elements

When encountering images or interactive elements, Copilot should:
1. Maintain existing alt text if present
2. Keep empty alt attributes if already specified
3. Ask for clarification if the accessibility purpose is unclear
4. Suggest proper syntax once the purpose is determined by the developer

#### Headings
All platforms should use headings for large text that breaks up chunks of content.

- Use semantic HTML heading tags (`<h1>`–`<h6>`) in a logical, nested order. Do not skip levels (e.g., `<h1>` to `<h4>`). Never use `<div>` or `<span>` as visual-only headers. Avoid empty or generic headings.

#### Forms - Labels
All form fields should have labels in the code. 
    - Use semantic HTML elements before applying ARIA roles.
    - All form fields must have programmatic labels:
        - Use <label for=""> or aria-labelledby
        - Placeholders must not be used as the only label

#### Forms - Errors & Helper Text
All form inputs must programmatically associate labels and helper text:
- Use `aria-describedby` or visually-associated text.

#### Error validation:
Errors need to be programmatically associated with each form field. Avoid automatically announcing errors as live regions.
- Use `aria-describedby` to link error messages to the form fields. Place the error text near the input and avoid using `aria-live` unless the error is critical and not tied to specific fields.

Error Announcement Priority:
1. Field-specific errors: Use aria-describedby to associate with inputs
2. Form-level errors: Use live regions only for critical, global error messages
3. Never use live regions for individual field validation

#### List Structure
This section describes how important list structure can be for users with disabilities
- Use native `<ul>` `<ol>` lists over `<div>`.


#### Reduced Motion:
Platforms should respect reduced motion settings to accommodate users with motion sensitivity.
- Use the `prefers-reduced-motion` media query to limit or disable animations, e.g., `@media (prefers-reduced-motion: reduce) { animation: none; }`.

#### Windows High Contrast Mode:
Using system colors ensures compatibility with Windows High Contrast Mode (Forced Colors) for better accessibility. This is really only needed for important things like component state or important component visual boundaries.
- Use system color keywords (e.g., `ButtonText`, `Highlight`, `CanvasText`) in CSS and detect forced colors with `@media (forced-colors: active) {}`. 

#### Cards 
For card components that do not have multiple CTAs in them or that have large touch targets, instead of wrapping the entire card, consider nesting a link inside a heading if the card has one. Create a large click area using pseudo selectors from that link inside the heading. 

##### Good example
`
<div class="card">
    <h2><a href="#">Some cool heading</a></h2>
    <!-- rest of card contents -->
</div>
`
---

### Copilot Response Requirements

Copilot-generated content must include:

1. Valid, accessible code using Arrow Design System components.
2. Inline comments explaining:
     - The purpose of accessibility features
     - Any trade-offs or browser quirks addressed
3. A plain-language summary of accessibility rationale.
4. A checklist that confirms rule conformance, for traceability
5. Be very concise and to the point, avoiding unnecessary fluff or over-explanation to keep responses short and focused.

Accessibility Verification:
- Keyboard-accessible interaction
- Visible focus indicators retained
- Valid labeling (aria-labelledby / label)
- Contrast ratios ≥ 4.5:1
- Proper ARIA use

