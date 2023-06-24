---
layout: post
branch: Twist
tag: Nanotips and FAQs
author: Daniel
title: FAQ 2 - How do I read maths in accessible ways?
buttonStyle: fg-blog-note
backgroundStyle: bg-blog-note
image: hand-braille.jpg
alt: hands going over a baille peice of paper
---

If you read my post on [FAQ 1]({{ site.baseurl }}{% link blog/twist/nanotip/_posts/2022-01-09-sight-loss-101.md %}) you may conclude that it is a very beginner level, very standard information pack. In this post, I write down my standard response to the second most frequently asked question, that is "How do I read maths?". While this is just as basic as the response given in FAQ 1, the topic of science accessibility is much more specialised. 
<!-- excerpt-end -->

Picking up the skills and getting familiar with some of the tools that enable screen reader users to read and write accessible maths notation is a significantly more challenging task, than learning to compose an email or text message. When I lost my sight, I first had to learn how to pour a drink, eat with a fork and knife, touch type, navigate the computer through keyboard commands, and finally, how to make mathematical notation accessible. Make no mistake, this process took years. However, as with everything, we need to start somewhere. So here is my entry level advice on making maths content accessible.

### Working With Maths notation as a blind person

Well done for taking up this exciting subject of astronomy. What helped me through out my physics degree was a markup language called [LaTeX](https://latex.org/forum/app.php/page/about-latex?sid=1ddd340f012284039ce0723393a9094b). If you haven’t done so, I’d recommend you to get familiar with it. Once you know how to create your own notes in LaTeX or get access to them through your lecturers, writing and reading mathematical notation will be definitely possible. However, writing in LaTeX real time can be slower than hand writing, so I would also urge you to get student support to get you a scribe, who can transfer notes from PDF documents, or the blackboard into LaTeX for you.

In addition, I heavily relied on an open source software called [LaTeX Access project](http://latex-access.sourceforge.net). I believe you can still find it on the web. Installing this and using alongside JAWS will be a big improvement in the experience, as this programme allows the screen reader to read out LaTeX code in a much more verbal language. For example, the code
```
\frac{1}{2}
```
 will be read as one half. This is a lot kinder to the ear, especially when it comes to more complex notation.

If the whole LaTeX plus LaTeX Access system does not work out for you, you can still rely on the [MathML](https://www.w3.org/Math/) standard. This is the standard language to write mathematical notation in web documents, such as HTML. Writing notes directly in HTML is not realistic, but there are lots of conversion tools that can automatically generate MathML rich HTML files. One of these are called [LaTeXML](https://latexml.mathweb.org/about). You can check this page too for [more information on LaTeXML.](https://math.nist.gov/~BMiller/LaTeXML/) Again, LaTeX is necessary here, but you can try to get these from your lecturers. JAWS and Voice Over will be able to read MathML to you, although to me it still feels a bit buggy here and there.

That’s it as a starter, but do let me know how you get on and if you have any more questions. I’m happy to clarify or assist you with some more technical or practical issues.