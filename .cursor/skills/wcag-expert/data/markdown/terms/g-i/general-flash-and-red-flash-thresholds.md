---
id: dfn-general-flash-and-red-flash-thresholds
term: general flash and red flash thresholds
---

# General Flash And Red Flash Thresholds

a [flash](https://www.w3.org/TR/WCAG22/#dfn-flashes) or rapidly changing image sequence is below the threshold (i.e., content **passes**) if any of the following are true:
   

   
   

      
      - there are no more than three **general flashes** and / or no more than three **red flashes** within any one-second period; or
      

      
      - the combined area of flashes occurring concurrently occupies no more than a total
         of .006 steradians within any 10 degree visual field on the screen (25% of any 10
         degree visual field on the screen) at typical viewing distance
      

      
   

   
   where:

   
   

      
      - A **general flash** is defined as a pair of opposing changes in [relative luminance](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance) of 10% or more of the maximum relative luminance (1.0) where the relative luminance of
         the darker image is below 0.80; and where "a pair of opposing changes" is an increase
         followed by a decrease, or a decrease followed by an increase, and
      

      
      - A **red flash** is defined as any pair of opposing transitions involving a saturated red
      

      
   

   
   *Exception:* Flashing that is a fine, balanced, pattern such as white noise or an alternating
      checkerboard pattern with "squares" smaller than 0.1 degree (of visual field at typical
      viewing distance) on a side does not violate the thresholds.
   

   
   Note 1For general software or web content, using a 341 x 256 pixel rectangle anywhere on the displayed screen area when the content is viewed at 1024 x 768 pixels will provide a good estimate of a 10 degree visual field for standard screen sizes and viewing distances (e.g., 15-17 inch screen at 22-26 inches). This resolution of 75 - 85 ppi is known to be lower, and thus more conservative than the nominal CSS pixel resolution of 96 ppi in CSS specifications. Higher resolutions displays showing the same rendering of the content yield smaller and safer images so it is lower resolutions that are used to define the thresholds.
   

   
   Note 2A transition is the change in relative luminance (or relative luminance/color for
      red flashing) between adjacent peaks and valleys in a plot of relative luminance (or
      relative luminance/color for red flashing) measurement against time. A flash consists
      of two opposing transitions.
   

   Note 3The new working definition in the field for **"pair of opposing transitions involving a saturated red"** (from WCAG 2.2) is a pair of opposing transitions where, one transition is either to or from a state with a value R/(R + G + B) that is greater than or equal to 0.8, and the difference between states is more than 0.2 (unitless) in the CIE 1976 UCS chromaticity diagram. [[ISO_9241-391](https://www.w3.org/TR/WCAG22/#bib-iso_9241-391)] 

   
   Note 4Tools are available that will carry out analysis from video screen capture. However,
      no tool is necessary to evaluate for this condition if flashing is less than or equal
      to 3 flashes in any one second. Content automatically passes (see #1 and #2 above).

---

📖 **Reference**: [WCAG 2.2 Glossary - general flash and red flash thresholds](https://www.w3.org/TR/WCAG22/#dfn-general-flash-and-red-flash-thresholds)
