---
id: dfn-relative-luminance
term: relative luminance
---

# Relative Luminance

the relative brightness of any point in a colorspace, normalized to 0 for darkest
      black and 1 for lightest white
   

   
  Note 1
   For the sRGB colorspace, the relative luminance of a color is defined as L = 0.2126
      * **R** + 0.7152 * **G** + 0.0722 * **B** where **R**, **G** and **B** are defined as:
   

   
   

      
      - if RsRGB [SRGB](https://www.w3.org/TR/WCAG22/#bib-srgb)].)
   

  

  Note 2Before May 2021 the value of 0.04045 in the definition was different (0.03928). It was taken from an older version of the specification and has been updated. It has no practical effect on the calculations in the context of these guidelines.

  
   Note 3Almost all systems used today to view web content assume sRGB encoding. Unless it
      is known that another color space will be used to process and display the content,
      authors should evaluate using sRGB colorspace. If using other color spaces, see [Understanding Success Criterion 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum).
   

   
   Note 4If dithering occurs after delivery, then the source color value is used. For colors
      that are dithered at the source, the average values of the colors that are dithered
      should be used (average R, average G, and average B).
   

   
   Note 5Tools are available that automatically do the calculations when testing contrast and
      flash.
   

   
   Note 6A [separate page giving the relative luminance definition using MathML](https://www.w3.org/TR/WCAG22/relative-luminance.html) to display the formulas is available.

---

📖 **Reference**: [WCAG 2.2 Glossary - relative luminance](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)
