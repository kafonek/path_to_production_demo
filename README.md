# path_to_production_demo
Jupyter Notebook path to production demo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kafonek/path_to_production_demo/master)


This repo is a reference example for a Jupyter disourse post about challenges in developing Notebooks for Enterprise user bases.  The crux of the issue is that the experience levels of users fall along a spectrum from "comfortable writing code from scratch" to "uncomfortable even seeing code" and everywhere in between.

Jupyter Notebooks are an invaluable and innovative resource for creating an introspective, exploratory, explanatory workflow.  Notebooks written with that style in mind typically have:

 * linear execution
 * small amount of code in each cell
 * descriptive output useful for sanity checks
 * Markdown narrative with table of contents
 * most data accessible in global scope for debug purposes
 
Jupyter Notebooks can also use ipywidgets to create rich interactive user interfaces that on par with many simple web applications.  Writing "web-app" Notebooks is popular  for many reasons, most of which revolve around Notebook authors getting the "product" out the door more quickly.  For instance, the "application logic" being used in the "web app" was probably prototyped in a Notebook already.  There is no (or significantly less) hassle with the overhead of setting up a web server, web framework stack, html/javascript file formatting, etc.  

