---
layout: post
author: Daniel Hajas
title: Custom domain and Google Analytics
branch: LogBook
tag: Site development
buttonStyle: fg-blog-sect
backgroundStyle: bg-blog-sect
image: google-analytics.png
alt: The Google Analytics logo, spelling the name of the service out, with a bar-chart underneath it.
---

Another step, another skill in the bag. Time to build live, measure constantly, and learn faster.

<!-- excerpt-end -->

Today marks the date when {{ site.brand }} transitioned from its Git Hub Pages [domain name](https://news.gandi.net/en/2021/08/how-to-use-subdomains-for-your-website/) to a custom domain. Say hello to [project27skills.com.](https://project27skills.com/) In addition, I also installed Google Analytics. 

### Our new address

Having a custom domain is an added cost. Our first fixed cost as a matter of fact. However, the return for visitors of the site is a more memorable, user friendly internet address. The return for us is two-fold. On one hand, it is an emotional reward. It marks the end of a phase, where we were tinkering in the garage. It's a moment of GOING LIVE. Scary, right? It is necessary though. We not only want to build {{ site.brand }}; we want to build something we think is valuable, measure what you think, and learn how we can create more value based on the measured feedback. 

Secondly, I never bought and hosted a website under a custom domain, so this was a great opportunity for learning. More about that in a minute.

### Google is watching

It was important to not only go live, but also to install tools that will help us with measuring engagement with the site. That's why from this version of the project, we are using Google Analytics. How useful it will be is yet to be seen, but nevertheless it was worth to learn how Google Analytics can be installed.

### Skills accounting

So what did I learn? First of all, that choosing a custom domain can be a frustrating experience. I also learnt about DNS records, and Jekyll environments.

#### Buying a domain

We wanted to host the site at the `project27.com` address, but guess what? It is already taken. Truth is, we had a nearly comical episode of finding the best alternative. We nearly rebranded to `Project26`, just to give you the scale of ideas we had to check for. I think eventually we stumbled upon an agreeable domain. Slightly longer, but more expressive. I also learnt that prices of domain names can range wildly from under £10, to many thousands of pounds per year. Crazy.

#### DNS records

Our community might know that we are hosting this site on Git Hub Pages. Luckily, GHP makes it super easy to [hook up your shiny new custom domain with your site.](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) The documentation proudly says, all you need to do is, "add a text file to your repository, call it CNAME, and add the custom domain name into the file". Easy! Well, in theory. What they don't tell you, only in the small-print, is that you'll also have to add to and edit the [DNS records](https://ns1.com/resources/dns-records-explained) of your domain. Wait what? What's a DNS? Yeah I pulled the same face, and thought why do computers always come with a small-print? 

Eventually, it turned out to be easy. Everything is easy once you know what to do. But imagine the anticipation, and frustration, when you find out that DNS propagation can take 24-72 hours, i.e. whatever changes you make, you will only find out whether it worked or not 1 day later. I was biting my nails down to their roots. The [`dig`](https://mediatemple.net/community/products/all/204644130/understanding-the-dig-command) unix command might be of help, but let's not go down this rabbit hole. Ohh, and did you know? DNS records have types. Many types... They also have a TTL. Sigh! So it's not as straight forward as the marketing teams like to put it, but it's certainly doable, and rewarding. Also, once you know how the whole process works, you know it all. It's a skill in the bag.

You also learn about subdomains, naked domains, and top level domains. Oh, I nearly missed Apex domains. Don't miss the Apex domain.

#### Jekyll environments

Google Analytics, or the installation of it is relatively straight forward in a manual site building environment. Essentially, you just need a Google Analytics account, a so called property within the account to point to the website you want to track, and a code that you insert onto your website. Again, there is small-print, but it's really straight forward. I found this post on [installing Google Analytics on a Jekyll site](https://desiredpersona.com/google-analytics-jekyll/) very useful.

However, the real useful learning is around [Jekyll environments](https://jekyllrb.com/docs/configuration/environments/). To avoid messing up your analytics data, it's important to exclude website activity during development and testing. That is, you really don't want analytics to track activity, when you are building and testing your site through the local host of Jekyll. To address this, it is useful to know that Jekyll, and most programming languages, will have different environments to work with. For example, a development and production environment. There are subtle differences. So subtle, that until now I didn't really appreciate the relevance of these environments. However, it is great that I am able to run a local server while I am building and testing a new feature, in the default  development environment, which I can set to ignore my analytics tools. Then, when I'm happy, I can switch to a production environment, build the site with analytics switched on, and deploy to the remote web server. This server is now found at the new address of the selected custom domain. Phew, isn't that wonderful? Okay, yes it's a bit of a nerd night, but the point is that the decision to go live, and switch to a more friendly web address, I learnt so many digital skills, which at first may look like unrelated skills. So is the annual fee worth it? Absolutely!

### Further reading

If you want to dig deeper, have a look at the following links:

1. [What are internet domains and subdomains?](https://news.gandi.net/en/2021/08/how-to-use-subdomains-for-your-website/)
2. [How to add and manage custom domains on Git Hub Pages?](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
3. [What are DNS records?](https://ns1.com/resources/dns-records-explained)
4. [What is the "dig" unix command?](https://mediatemple.net/community/products/all/204644130/understanding-the-dig-command)
5. [What are Jekyll environments?](https://jekyllrb.com/docs/configuration/environments/)
6. [How to get started with Google Analytics on Jekyll](https://desiredpersona.com/google-analytics-jekyll/)