# Lab 7: Fuzzing for Input Validation Bugs

**Student Name:** Navaneeth Tanuboddi  
**SRN:** PES1UG24CS709  
**Assigned Topic / Repo:** `L6_L7_45_mobile_data_plan`

---

## 🎯 Lab Objectives
- Understand the methodology and purpose of fuzz testing using property-based fuzzing.
- Use the **Hypothesis** library in Python to generate random, unexpected, and malformed inputs.
- Detect input validation edge-case bugs and unhandled exceptions (e.g., `NoneType`, empty strings, missing delimiters, malformed numeric formats, division by zero).
- Apply defensive programming techniques to harden functions against unexpected inputs and crashes.

---

## 📁 Files in this Directory
- **`mobile_data_plan.py`**: Hardened Python script with defensive validation checks.
- **`test_mobile_data_plan.py`**: Fuzz test suite using Hypothesis (`@given(st.text() | st.none())`).
- **`Lab7_Fuzzing_Report.pdf`**: Complete PDF document containing all lab execution steps, technical explanations, and embedded screenshots (Steps 2, 4, 5, and 6).

---

## 🔬 Lab Steps & Verification Summary

1. **Step 1: Install Dependencies**
   - Installed `hypothesis` and `pytest`.
2. **Step 2: Run Buggy Application**
   - Verified initial execution with nominal input (`python mobile_data_plan.py`).
3. **Step 3 & 4: Implement Hypothesis Fuzz Tests & Detect Bugs**
   - Wrote `@given(st.text() | st.none())` tests.
   - Discovered edge cases failing with `ValueError`, `AttributeError`, and `ZeroDivisionError`.
4. **Step 5: Harden Application (`mobile_data_plan.py`)**
   - Implemented strict type validation, safe splitting, empty checking, float/int parsing bounds, and NaN/Inf sanitization.
5. **Step 6: Re-run Fuzz Tests**
   - Executed `pytest test_mobile_data_plan.py`.
   - **Result:** 100% pass rate (`3 passed in 0.29s`) with zero crashes.

> **Note:** All terminal screenshots for Steps 2, 4, 5, and 6 are compiled into **`Lab7_Fuzzing_Report.pdf`** in this directory.
