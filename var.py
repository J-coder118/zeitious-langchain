CTA_1 = "The Top Hack Business Owners and Career Professionals Use To Reinvent Themselves So That They Are Recognized Not Just For Their Achievements Or Title But For Who They Are— Their Ideas, Their Character, Their Unique Perspective"

CTA_2 = """You are a seasoned coach. You are assisting a client (me) in identifying the exact way my client thinks about this challenge in their words. Please List out TEN hell experiences my client goes through DAILY related to this problem: LIST YOUR PROBLEM HERE. e.g. They need life insurance but don't have it.
Imagine they are talking with a friend at Starbucks about this problem. Exactly what would they say? (Remember they are not a professional)
Please share 10 different ways this hits them on a daily basis.”
Remember that you can also tell chatty to speak to the pain of someone who is a professional, or "doing well" so it doesn't go  for the bottom half of the pool."""

VIDEO_CTA = """
generate 6 paragraphs of text.
In This ONE DAY LIVE ONLINE Challenge You Will Learn:

STEP 1: The step by step game plan our clients use to create FREELY and bring their ideas to life without fear or restrictions because they are finissshheeeddd with just going through the motions, hiding their brilliance or feeling stagnant.

STEP 2: How you can create genuine, deep connections with people— relationships where you share your true thoughts and feelings, and they can do the same. Even if you have held yourself back because of people’s opinions for years.

Step 3: The 2-3 small tweaks you can make to how you think and operate at work, and at home that can allow you to reconnect with a deep sense of purpose, and passion, in things that deeply matter to you within the next one month… even if you have been buried in busyness for months.

Step 4: How to stop constantly chasing deadlines and finally have the most important things FIRST in your life. Your faith. Your family. Your impact. Your fun. Your money. 

Step 5: The real reason why you feel so frustrated when people congratulate you and then tell you to “settle down” because of your achievements when you know deep down that there is more — AND what you can do to let go of their expectations and start creating at the level you envision for yourself TODAY…

Step 6: AND…. how to do all of this while feeling that buzz of excitement about what you are doing with your time and without compromising on your values; or needing to ditch your achievements/pretend to be struggling when you are not. We know you are already winning. Show up with your full chest!

"""

VAR_3 = """

[author_name] is recognized as one of the leading voices in the personal development space, exemplified by her selection as 1 of 50 women for the SUCCESS Magazine’s 2023 Women of Influence Awards. She is also the CEO of the 74th fastest-growing company in Canada and the creator of the Diamond Effect™ Neuroscience System.

She has trained over 50,000+ business owners and career professionals in how to use the power of neuroscience to master themselves, unlock their full potential, and confidently step into new realms of success and fulfillment.

She has helped clients increase their net worth by tens of millions of dollars, pay off millions of dollars worth of debt and do this without living on rice and beans. Using the principles she teaches, [author_name] went from being stuck in tens of thousands of debt, having no food for her family to 11 streams of income, multiple real estate properties and running a company that does multiple seven figures a year - In the span of FOUR years. It's your turn!"""


HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta name="author" content="ThemeStarz" />

    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:400,600,700" />
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css" type="text/css" />
    <link rel="stylesheet" href="assets/font-awesome/css/fontawesome-all.min.css" />
    <link rel="stylesheet" href="assets/css/magnific-popup.css" />
    <link rel="stylesheet" href="assets/css/owl.carousel.min.css" />
    <link rel="stylesheet" href="assets/css/style.css" />
    <title>LifeCoach - One Page Coach & Mentor Template</title>

    <style>
    /*----------------------------------------------------------------------------------------------------------------------
Project:	    LifeCoach
Version:        1.0.0

Default Color   #f4b200;

Body copy:		'Poppins', sans-serif; 14px;
Headers:		'Nunito', sans-serif;

----------------------------------------------------------------------------------------------------------------------*/

/*----------------------------------------------------------------------------------------------------------------------
[Table of contents]

A. Basic Styling
  -- Styling

B. Helpers
  -- Animations
  -- Borders
  -- Colors
  -- Column Count
  -- Transitions
  -- Background
  -- Headings
  -- Height
  -- Margin
  -- No Gutter
  -- Opacity
  -- Overflow
  -- Padding
  -- Position
  -- Shadow
  -- Shape Mask
  -- Typography
  -- Title
  -- Transitions
  -- Utilities
  -- Width
  -- Z-Index

C. Components
  -- Block
  -- Blockquote
  -- Box
  -- Buttons
  -- Card
  -- Circle
  -- Forms
  -- Inputs
  -- Item
  -- List
  -- Map
  -- Hero
  -- Navbar
  -- Page
  -- Partners
  -- Plugins
  -- Price Box
  -- Progress
  -- Promo Numbers
  -- Select
  -- Slider
  -- Tabs

D. Plugins Styles
  -- Magnific Popup
  -- Owl Carousel

E. Template Specific Elements
  -- Price Box
  -- Other
  -- Story


----------------------------------------------------------------------------------------------------------------------*/

/***********************************************************************************************************************
A. Basic Styling
***********************************************************************************************************************/

/*-------------------------------------------
  -- Styling - Colors, Font Size, Font Family
-------------------------------------------*/

body {
    color: #191919;
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
    font-size: .9375rem;
    margin: 0;
    padding: 0;
}

html {
    font-size: 80%;
}

h1, h2, h3, h4, h5 {
    font-family: 'Nunito', sans-serif;
    font-weight: 600;
}

h1, .ts-h1 {
    font-size: 2.5rem;
}

h2, .ts-h2 {
    font-size: 1.5rem;
}

h3, .ts-h3 {
    font-size: 1.25rem;
    margin-bottom: 1.5625rem;
}

h4, .ts-h4 {
    margin-bottom: 1.875rem;
}

h5, .ts-h5 {
    font-size: 1rem;
    font-weight: 600;
}

h6, .ts-h6 {
    font-size: .9375rem;
}

/* NEW */

/***********************************************************************************************************************
B. Helpers
***********************************************************************************************************************/

/*-------------------------------------------
  -- Animations
-------------------------------------------*/

[data-animate] {
    opacity: 0;
    animation-fill-mode: forwards;
    animation-duration: .6s;
    animation-timing-function: ease;
}

/* Fade In Up */

@keyframes ts-fadeInUp {
    from {
        opacity: 0;
        transform: translate3d(0, 1.25rem, 0);
    }

    to {
        opacity: 1;
        transform: translate3d(0, 0, 0);
    }
}

.ts-fadeInUp {
    animation-name: ts-fadeInUp;
}

/* Fade In Down */

@keyframes ts-fadeInDown {
    from {
        opacity: 0;
        transform: translate3d(0, -1.25rem, 0);
    }

    to {
        opacity: 1;
        transform: translate3d(0, 0, 0);
    }
}

.ts-fadeInDown {
    animation-name: ts-fadeInDown;
}

/* Fade In Left */

@keyframes ts-fadeInLeft {
    from {
        opacity: 0;
        transform: translate3d(-1.25rem, 0, 0);
    }

    to {
        opacity: 1;
        transform: translate3d(0, 0, 0);
    }
}

.ts-fadeInLeft {
    animation-name: ts-fadeInLeft;
}

/* Fade In Right */

@keyframes ts-fadeInRight {
    from {
        opacity: 0;
        transform: translate3d(1.25rem, 0, 0);
    }

    to {
        opacity: 1;
        transform: translate3d(0, 0, 0);
    }
}

.ts-fadeInRight {
    animation-name: ts-fadeInRight;
}

/* Zoom In */

@keyframes ts-zoomIn {
    from {
        opacity: 0;
        transform: scale(.5);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

.ts-zoomIn {
    animation-name: ts-zoomIn;
}

/* Zoom Out In */

@keyframes ts-zoomOutIn {
    from {
        opacity: 0;
        transform: scale(1.1);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

.ts-zoomOutIn {
    animation-name: ts-zoomOutIn;
}

/* Zoom In Short */

@keyframes ts-zoomInShort {
    from {
        opacity: 0;
        transform: scale(.9);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

.ts-zoomInShort {
    animation-name: ts-zoomInShort;
}

/*-------------------------------------------
  -- Borders
-------------------------------------------*/

.ts-border-radius__sm {
    border-radius: .125rem;
    overflow: hidden;
}

.ts-border-radius__md {
    border-radius: .25rem;
    overflow: hidden;
}

.ts-border-radius__lg {
    border-radius: .5rem;
    overflow: hidden;
}

.ts-border-radius__xl {
    border-radius: .75rem;
    overflow: hidden;
}

.ts-border-radius__pill {
    border-radius: 6.25rem !important;
    overflow: hidden;
}

.ts-border-radius__round-shape {
    border-radius: 187.5rem;
    overflow: hidden;
}

.ts-border-none {
    border: none;
}

.ts-border-bottom {
    border-bottom: .0625rem solid rgba(0, 0, 0, .1);
}

.ts-font-color__white {
    color: #fff;
}

.ts-font-color__black {
    color: #000;
}

.ts-font-color__primary {
    color: #f4b200;
}

/*-------------------------------------------
  -- Background
-------------------------------------------*/

[data-bg-image] {
    background-size: cover;
    background-position: 50%;
}

.ts-background {
    bottom: 0;
    left: 0;
    height: 100%;
    overflow: hidden;
    position: absolute;
    width: 100%;
    z-index: -2;
}

.ts-background .ts-background {
    height: 100%;
    width: 100%;
}

.ts-background-repeat {
    background-repeat: repeat;
    background-size: inherit;
}

.ts-background-repeat .ts-background-image {
    background-repeat: repeat;
    background-size: inherit;
}

.ts-background-image, .ts-img-into-bg {
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 50%;
    height: 100%;
    overflow: hidden;
    width: 100%;
}

.ts-background-image img, .ts-img-into-bg img {
    display: none;
}

.ts-background-original-size {
    background-size: inherit;
}

.ts-background-size-cover {
    background-size: cover;
}

.ts-background-size-contain {
    background-size: contain;
}

.ts-background-repeat-x {
    background-repeat: repeat-x;
}

.ts-background-repeat-y {
    background-repeat: repeat-y;
}

.ts-background-repeat-repeat {
    background-repeat: repeat;
    background-size: inherit;
}

.ts-background-position-top {
    background-position: top;
}

.ts-background-position-center {
    background-position: center;
}

.ts-background-position-bottom {
    background-position: bottom;
}

.ts-background-position-left {
    background-position-x: left !important;
}

.ts-background-position-right {
    background-position-x: right !important;
}

.ts-background-particles {
    height: 120%;
    left: 0;
    margin-left: -10%;
    margin-top: -10%;
    overflow: hidden;
    position: absolute;
    top: 0;
    width: 120%;
    z-index: 1;
}

.ts-background-is-dark {
    color: #fff;
}

.ts-background-is-dark .form-control {
    box-shadow: 0 0 0 .125rem rgba(255, 255, 255, .2);
}

.ts-background-is-dark .form-control:focus {
    box-shadow: 0 0 0 .125rem rgba(255, 255, 255, .4);
}

.ts-background-is-dark .ts-btn-border-muted {
    border-color: rgba(255, 255, 255, .1);
}

.ts-video-bg {
    height: 100%;
}

.ts-video-bg .fluid-width-video-wrapper {
    height: 100%;
}

/*-------------------------------------------
  -- Height
-------------------------------------------*/

.ts-height__50px {
    height: 3.125rem;
}

.ts-height__100px {
    height: 6.25rem;
}

.ts-height__150px {
    height: 9.375rem;
}

.ts-height__200px {
    height: 12.5rem;
}

.ts-height__250px {
    height: 15.625rem;
}

.ts-height__300px {
    height: 18.75rem;
}

.ts-height__350px {
    height: 21.875rem;
}

.ts-height__400px {
    height: 25rem;
}

.ts-height__450px {
    height: 28.125rem;
}

.ts-height__500px {
    height: 31.25rem;
}

.ts-height__600px {
    height: 37.5rem;
}

.ts-height__700px {
    height: 43.75rem;
}

.ts-height__800px {
    height: 50rem;
}

.ts-height__900px {
    height: 56.25rem;
}

.ts-height__1000px {
    height: 62.5rem;
}

/*-------------------------------------------
  -- Margin
-------------------------------------------*/

.ts-mt__0 {
    margin-top: 0 !important;
}

.ts-mr__0 {
    margin-right: 0 !important;
}

.ts-mb__0 {
    margin-bottom: 0 !important;
}

.ts-ml__0 {
    margin-left: 0 !important;
}

/*-------------------------------------------
  -- No Gutters - Removes padding from col*
-------------------------------------------*/

.no-gutters {
    margin-right: 0;
    margin-left: 0;
}

.no-gutters > .col, .no-gutters > [class*="col-"] {
    padding-right: 0;
    padding-left: 0;
}

/*-------------------------------------------
  -- Opacity
-------------------------------------------*/

.ts-opacity__5 {
    opacity: .05;
}

.ts-opacity__10 {
    opacity: .1;
}

.ts-opacity__20 {
    opacity: .2;
}

.ts-opacity__30 {
    opacity: .3;
}

.ts-opacity__40 {
    opacity: .4;
}

.ts-opacity__50 {
    opacity: .5;
}

.ts-opacity__60 {
    opacity: .6;
}

.ts-opacity__70 {
    opacity: .7;
}

.ts-opacity__80 {
    opacity: .8;
}

.ts-opacity__90 {
    opacity: .9;
}

/*-------------------------------------------
  -- Overflow
-------------------------------------------*/

.ts-overflow__hidden {
    overflow: hidden;
}

.ts-overflow__visible {
    overflow: visible;
}

/*-------------------------------------------
  -- Padding
-------------------------------------------*/

.ts-pt__0 {
    padding-top: 0 !important;
}

.ts-pr__0 {
    padding-right: 0 !important;
}

.ts-pb__0 {
    padding-bottom: 0 !important;
}

.ts-pl__0 {
    padding-left: 0 !important;
}

/*-------------------------------------------
  -- Position
-------------------------------------------*/

/* Top */

.ts-top__0 {
    top: 0%;
}

.ts-top__50 {
    top: 50%;
}

.ts-top__100 {
    top: 100%;
}

/* Right */

.ts-right__0 {
    right: 0%;
}

.ts-right__50 {
    right: 50%;
}

.ts-right__100 {
    right: 100%;
}

.ts-right__inherit {
    right: inherit;
}

/* Bottom */

.ts-bottom__0 {
    bottom: 0%;
}

.ts-bottom__50 {
    bottom: 50%;
}

.ts-bottom__100 {
    bottom: 100%;
}

/* Left */

.ts-left__0 {
    left: 0%;
}

.ts-left__50 {
    left: 50%;
}

.ts-left__100 {
    left: 100%;
}

.ts-left__inherit {
    left: inherit;
}

.ts-push-left__100 {
    transform: translateX(100%);
}

.ts-push-down__50 {
    transform: translateY(50%);
}

/*-------------------------------------------
  -- Shadow
-------------------------------------------*/

.ts-shadow__sm {
    box-shadow: 0 .125rem .3125rem rgba(0, 0, 0, .1);
}

.ts-shadow__md {
    box-shadow: .125rem .1875rem .9375rem rgba(0, 0, 0, .15);
}

.ts-shadow__lg {
    box-shadow: .375rem .3125rem 1.5625rem rgba(0, 0, 0, .2);
}

.ts-shadow__none {
    box-shadow: none !important;
}

/*-------------------------------------------
  -- Typography
-------------------------------------------*/

a {
    color: #f4b200;
    transition: .3s ease;
}

a:hover {
    color: rgb(194, 142, 0);
    text-decoration: none;
}

p {
    line-height: 1.6875rem;
    margin-bottom: 1.875rem;
    color: rgba(0, 0, 0, .5);
}

.ts-font-weight__normal {
    font-weight: normal;
}

.ts-font-weight__light {
    font-weight: lighter;
}

.ts-font-weight__bold {
    font-weight: bold;
}

.ts-text-small {
    font-size: .8125rem !important;
}

.ts-xs-text-center {
}

/*-------------------------------------------
  -- Title
-------------------------------------------*/

.ts-title {
}

.ts-title h5 {
    font-weight: normal;
    opacity: .5;
}

/*-------------------------------------------
  -- Utilities
-------------------------------------------*/

.ts-element {
    position: relative;
}

/* Social Icons */

.ts-social-icons {
    font-size: 120%;
}

.ts-social-icons a {
    padding: .125rem .25rem;
    color: #9e9e9e;
}

/* Overlay */

.ts-has-overlay {
    position: relative;
}

.ts-has-overlay:after {
    background-color: #000;
    content: "";
    height: 100%;
    left: 0;
    opacity: .5;
    position: absolute;
    top: 0;
    width: 100%;
    z-index: -1;
}

/* Flip x */

.ts-flip-x {
    transform: scaleY(-1);
}

/* Flip Y */

.ts-flip-y {
    transform: scaleX(-1);
}

.ts-video-bg {
    height: 100%;
}

.ts-video-bg .fluid-width-video-wrapper {
    height: 100%;
}

.ts-video-bg iframe {
    border: 0;
    height: 100%;
    width: 100%;
}

/*-------------------------------------------
  -- Width
-------------------------------------------*/

.ts-width__10px {
    width: .625rem;
}

.ts-width__20px {
    width: 1.25rem;
}

.ts-width__30px {
    width: 1.875rem;
}

.ts-width__40px {
    width: 2.5rem;
}

.ts-width__50px {
    width: 3.125rem;
}

.ts-width__100px {
    width: 6.25rem;
}

.ts-width__200px {
    width: 12.5rem;
}

.ts-width__300px {
    width: 18.75rem;
}

.ts-width__400px {
    width: 25rem;
}

.ts-width__500px {
    width: 31.25rem;
}

.ts-width__inherit {
    width: inherit !important;
}

.ts-width__auto {
    width: auto !important;
}

/*-------------------------------------------
  -- Z-index
-------------------------------------------*/

.ts-z-index__-1 {
    z-index: -1 !important;
}

.ts-z-index__0 {
    z-index: 0 !important;
}

.ts-z-index__1 {
    z-index: 1 !important;
}

.ts-z-index__2 {
    z-index: 2 !important;
}

.ts-z-index__1000 {
    z-index: 1000 !important;
}

/***********************************************************************************************************************
C. Components
***********************************************************************************************************************/

/*-------------------------------------------
  -- Block
-------------------------------------------*/

.ts-block {
    padding-bottom: 5rem;
    padding-top: 5rem;
    position: relative;
    /*
  &:after {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg'  width='103.987' height='105.599'%3E%3cpath fill='var(--color-primary-svg)' d='M101.017 45.961c-10.338 22.34-33.156 61.239-62.326 59.586-31.984-1.803-44.52-48.772-36.182-73.996 15.682-47.439 120.287-40.376 98.508 14.41-10.998 23.766 1.923-4.836 0 0z'/%3E%3c/svg%3E");
  }
  */
}

.ts-block-inside {
    padding: 1.25rem;
    position: relative;
}

section {
    position: relative;
}

/*-------------------------------------------
  -- Blockquote
-------------------------------------------*/

blockquote {
    font-size: 1.125rem;
    position: relative;
    padding-bottom: 2rem;
}

blockquote [class*="ts-circle"] {
    box-shadow: .375rem .3125rem 1.5625rem rgba(0, 0, 0, .2);
    position: relative;
    z-index: 2;
    margin-top: 1rem;
}

blockquote p {
    background-color: #f1f1f1;
    border-radius: .25rem;
    margin-top: -2.5rem;
    padding: 2.5rem;
    position: relative;
    z-index: 1;
}

blockquote p:after {
    border-color: #f1f1f1 transparent transparent transparent;
    border-style: solid;
    border-width: .8125rem .8125rem 0 .8125rem;
    content: "";
    width: 0;
    height: 0;
    position: absolute;
    left: 0;
    right: 0;
    margin: auto;
    bottom: -0.8125rem;
}

blockquote h4 {
    margin-bottom: .3125rem;
}

blockquote h6 {
    opacity: .5;
}

.blockquote-footer {
    color: inherit;
}

.blockquote-footer:before {
    display: none;
}

.ts-carousel-blockquote .owl-item figure, .ts-carousel-blockquote .owl-item p,
.ts-carousel-blockquote .owl-item .blockquote-footer {
    opacity: 0;
    transition: .6s ease;
    transform: translateY(.625rem);
}

.ts-carousel-blockquote .owl-item.active figure,
.ts-carousel-blockquote .owl-item.active p,
.ts-carousel-blockquote .owl-item.active .blockquote-footer {
    opacity: 1;
    transform: translateY(0);
}

.ts-carousel-blockquote .owl-item.active p {
    transition-delay: .1s;
}

.ts-carousel-blockquote .owl-item.active .blockquote-footer {
    transition-delay: .2s;
}

/*-------------------------------------------
  -- Box
-------------------------------------------*/

.ts-box {
    background-color: #fff;
    border-radius: .25rem;
    margin-bottom: 1.875rem;
    box-shadow: .125rem .1875rem .9375rem rgba(0, 0, 0, .15);
    padding: 1.5625rem;
}

/*-------------------------------------------
  -- Buttons
-------------------------------------------*/

.btn {
    border-radius: 6.25rem;
    border-width: .125rem;
    box-shadow: .125rem .1875rem .9375rem rgba(0, 0, 0, .15);
    font-weight: 600;
    font-size: .9375rem;
    padding: .5rem 1.25rem;
    position: relative;
    outline: none !important;
}

.btn:hover .fa-arrow-right {
    transform: translateX(.5rem);
}

.btn .fa-arrow-right {
    transition: .6s cubic-bezier(.85, -0.37, .17, 1.45);
    transform: translateX(0) rotate(.02deg);
}

.btn span {
    transition: .3s ease;
}

.btn .status {
    bottom: 0;
    height: 1.375rem;
    left: 0;
    margin: auto;
    position: absolute;
    top: 0;
    right: 0;
    width: 1.5rem;
}

.btn .status .spinner {
    left: .3125rem;
    transition: .3s ease;
    top: .1875rem;
    position: absolute;
    opacity: 0;
}

.btn .status .status-icon {
    border-radius: 50%;
    left: 0;
    opacity: 0;
    font-size: .625rem;
    padding: .25rem .4375rem;
    position: relative;
    transition: .3s ease;
    z-index: 1;
    transform: scale(0);
}

.btn .status .status-icon.valid {
    background-color: var(--green);
}

.btn .status .status-icon.invalid {
    background-color: var(--red);
}

.btn.processing span {
    opacity: .2;
}

.btn.processing .spinner {
    opacity: 1;
}

.btn.done .ts-spinner {
    opacity: 0;
}

.btn.done .status-icon {
    transform: scale(1);
    opacity: 1;
}

.btn-primary:hover, .btn-primary:focus, .btn-primary:active {
    /*background-color: darken( var(--color-primary), 20% );
    border-color: darken( var(--color-primary), 20% );*/
    background-color: #f4b200;
    border-color: #f4b200;
    box-shadow: .125rem .1875rem .9375rem rgba(0, 0, 0, .3);
}

.btn-primary {
    background-color: #f4b200;
    border-color: #f4b200;
    color: #fff;
}

.btn-primary.disabled, .btn-primary:disabled {
    background-color: rgb(194, 142, 0);
    border-color: rgb(194, 142, 0);
}

.btn-primary:not(:disabled):not(.disabled):active:focus,
.btn-primary:not(:disabled):not(.disabled).active:focus,
.show > .btn-primary.dropdown-toggle:focus {
    background-color: rgb(194, 142, 0);
    border-color: rgb(173, 127, 0);
    box-shadow: 0 .1875rem .9375rem rgba(0, 0, 0, .2);
}

.btn-primary:not(:disabled):not(.disabled):active,
.btn-primary:not(:disabled):not(.disabled).active,
.show > .btn-primary.dropdown-toggle {
    background-color: rgb(194, 142, 0);
    border-color: rgb(194, 142, 0);
    box-shadow: 0 .1875rem .9375rem rgba(0, 0, 0, .2);
}

.btn-dark {
    background-color: #191919;
    border-color: #191919;
}

.btn-outline-primary {
    border-color: #f4b200;
    color: #f4b200;
}

.btn-outline-primary:hover {
    background-color: #f4b200;
    border-color: #f4b200;
}

.btn-outline-primary:not(:disabled):not(.disabled):active:focus {
    background-color: #f4b200;
    border-color: #f4b200;
    box-shadow: 0 0 0 .2rem rgba(244, 178, 0, .5);
}

.btn-lg {
    padding: .75rem 1.5rem;
    font-size: 1.125rem;
}

.btn-sm {
    font-size: .8125rem;
    padding: .375rem 1rem;
}

.btn-xs {
    font-size: .75rem;
    font-weight: 600;
    padding: .125rem .6875rem;
    text-transform: uppercase;
}

[class*="btn-outline-"] {
    box-shadow: none;
}

.ts-btn-border-muted {
    border-color: rgba(25, 25, 25, .1);
}

/*-------------------------------------------
  -- Card
-------------------------------------------*/

.card {
    backface-visibility: hidden;
    border: none;
    box-shadow: .125rem .1875rem .9375rem rgba(0, 0, 0, .15);
    margin-bottom: 1.875rem;
    overflow: hidden;
}

.card-columns .card {
    margin-bottom: 1.25rem;
}

.card-body, .card-footer, .card-header {
    padding: 1.5625rem;
}

.ts-cards-same-height > div[class*='col-'] {
    display: flex;
}

.ts-cards-same-height > div[class*='col-'] .card {
    width: 100%;
}

.ts-card__flat {
    border-radius: 0;
    box-shadow: none;
}

.ts-card__flat .card-footer {
    background-color: transparent;
    border: none;
}

.ts-card__image {
}

/*-------------------------------------------
  -- Circle
-------------------------------------------*/

.ts-circle__xs {
    border-radius: 50%;
    display: inline-block;
    height: 3rem;
    flex: 0 0 3rem;
    overflow: hidden;
    text-align: center;
    line-height: 3rem;
    width: 3rem;
}

.ts-circle__sm {
    border-radius: 50%;
    display: inline-block;
    height: 4.375rem;
    flex: 0 0 4.375rem;
    overflow: hidden;
    text-align: center;
    line-height: 4.375rem;
    width: 4.375rem;
}

.ts-circle__md {
    border-radius: 50%;
    display: inline-block;
    height: 6.25rem;
    flex: 0 0 6.25rem;
    overflow: hidden;
    text-align: center;
    line-height: 6.25rem;
    width: 6.25rem;
}

.ts-circle__lg {
    border-radius: 50%;
    display: inline-block;
    height: 8.125rem;
    flex: 0 0 8.125rem;
    overflow: hidden;
    text-align: center;
    line-height: 8.125rem;
    width: 8.125rem;
}

.ts-circle__xl {
    border-radius: 50%;
    display: inline-block;
    height: 10rem;
    flex: 0 0 10rem;
    overflow: hidden;
    text-align: center;
    line-height: 10rem;
    width: 10rem;
}

.ts-circle__xxl {
    border-radius: 50%;
    display: inline-block;
    height: 15.625rem;
    flex: 0 0 15.625rem;
    overflow: hidden;
    text-align: center;
    line-height: 15.625rem;
    width: 15.625rem;
}

/*-------------------------------------------
  -- Forms
-------------------------------------------*/

form.ts-labels-inside-input .form-group,
.ts-form.ts-labels-inside-input .form-group {
    position: relative;
}

form.ts-labels-inside-input .form-group label,
.ts-form.ts-labels-inside-input .form-group label {
    line-height: 2.625rem;
    left: .8125rem;
    opacity: .4;
    pointer-events: none;
    position: absolute;
    top: 0;
    transition: .3s ease;
}

form.ts-labels-inside-input .form-group label.focused,
.ts-form.ts-labels-inside-input .form-group label.focused {
    top: -2.1875rem;
    left: 0;
    font-size: .75rem;
    opacity: 1;
}

.form-control {
    border: 0;
    box-shadow: 0 0 0 .125rem rgba(0, 0, 0, .2);
    border-radius: .125rem;
    padding: .5625rem .75rem;
}

.form-control:focus {
    box-shadow: 0 0 0 .125rem rgba(0, 0, 0, .4);
}

.form-group {
    margin-bottom: 1.5625rem;
}

.form-group label {
    font-size: .8125rem;
}

.ts-gallery {
    position: relative;
}

.ts-gallery .ts-gallery__image {
    background-color: #191919;
    color: #fff;
    display: block;
    height: 28rem;
    overflow: hidden;
}

.ts-gallery .ts-gallery__image:hover .ts-img-into-bg {
    opacity: .3;
    transform: scale(1.1);
}

.ts-gallery .ts-gallery__caption {
    padding: 3rem;
    bottom: 0;
    left: 0;
    position: absolute;
    z-index: 2;
}

.ts-gallery .ts-img-into-bg {
    opacity: .6;
    transition: 1s cubic-bezier(.23, .05, .17, 1.02);
    transform: scale(1.03);
}

/*-------------------------------------------
  -- Inputs
-------------------------------------------*/

.ts-input__static {
    pointer-events: none;
    box-shadow: none;
}

.ts-inputs__transparent input, .ts-inputs__transparent textarea {
    background-color: transparent;
    color: #fff;
}

.ts-inputs__transparent input:active, .ts-inputs__transparent input:focus,
.ts-inputs__transparent textarea:active, .ts-inputs__transparent textarea:focus {
    background-color: transparent;
    color: #fff;
}

.ts-item {
    height: 100%;
    padding-bottom: 1.875rem;
}

.ts-item-content {
    display: flex;
    flex-direction: column;
    height: 100%;
}

.ts-item-header {
    margin-bottom: 1.5625rem;
    position: relative;
}

.ts-item-header .icon {
    position: relative;
    display: inline-block;
}

.ts-item-header .icon .step {
    background-color: #f4b200;
    top: 0;
    box-shadow: .125rem .1875rem .9375rem rgba(0, 0, 0, .15);
    border-radius: 50%;
    color: #fff;
    font-weight: 600;
    line-height: 1.875rem;
    right: 0;
    height: 1.875rem;
    position: absolute;
    text-align: center;
    width: 1.875rem;
}

.ts-item-body {
    flex: 1 1 auto;
}

.ts-item-footer {
}

/*-------------------------------------------
  -- List
-------------------------------------------*/

ul {
    line-height: 2.5rem;
    list-style: none;
    padding-left: 0;
}

ul.ts-list-colored-bullets li:before {
    content: "•";
    color: #f4b200;
    vertical-align: middle;
    font-size: 1.75rem;
    padding-right: .75rem;
}

ul.ts-list-divided li {
    border-bottom: .0625rem solid rgba(0, 0, 0, .1);
    padding-bottom: .3125rem;
    padding-top: .3125rem;
}

ul.ts-list-divided li:last-child {
    border-bottom: none;
}

/*-------------------------------------------
  -- Loading Screen
-------------------------------------------*/

body.has-loading-screen:before {
    background-color: #000;
    content: "";
    height: 100%;
    right: 0;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 9999;
    transition: 1.5s ease;
    opacity: 1;
}

body.has-loading-screen:after {
    content: url("../../assets/img/loading.svg");
    height: 2.5rem;
    width: 2.5rem;
    position: fixed;
    margin: auto;
    bottom: 0;
    left: 0;
    right: 0;
    opacity: 1;
    transform: scale(1);
    transition: 1.5s ease;
    top: 0;
    z-index: 10000;
}

body.has-loading-screen.loading-done:before {
    width: 0;
}

body.has-loading-screen.loading-done:after {
    transform: scale(0);
    opacity: 0;
}

/*-------------------------------------------
  -- Map
-------------------------------------------*/

.map {
    min-height: 12.5rem;
}

.map a[href^="http://maps.google.com/maps"] {
    display: none !important;
}

.map a[href^="https://maps.google.com/maps"] {
    display: none !important;
}

.map .gmnoprint a, .map .gmnoprint span, .map .gm-style-cc {
    display: none;
}

/*-------------------------------------------
  -- Hero
-------------------------------------------*/

#ts-hero {
    position: relative;
    overflow: hidden;
}

#ts-hero .ts-background-image {
    background-position: top center;
}

/*-------------------------------------------
  -- Navbar
-------------------------------------------*/

.navbar {
    font-size: .875rem;
    font-weight: 500;
    padding-bottom: 2rem;
    padding-top: 2rem;
    transition: .3s ease;
}

.navbar.in {
    padding-bottom: 1rem;
    padding-top: 1rem;
}

.navbar.in .ts-background {
    opacity: 1 !important;
}

.navbar .ts-background {
    transition: 1s ease;
}

[class*="navbar-expand"] .navbar-nav .nav-link {
    padding-top: .5rem;
    padding-bottom: .5rem;
    border-bottom: .0625rem solid rgba(0, 0, 0, .1);
}

/*XL*/

/*LG*/

/*MD*/

/*SM*/

/*-------------------------------------------
  -- Page
-------------------------------------------*/

.ts-page-wrapper {
    overflow: hidden;
}

/*-------------------------------------------
  -- Partners
-------------------------------------------*/

.ts-partners a {
    display: block;
    padding: .625rem .3125rem;
}

/*-------------------------------------------
  -- Plugins
-------------------------------------------*/

.tv-site-widget {
    border: none !important;
}

iframe div {
    border: none;
}

/*-------------------------------------------
  -- Progress
-------------------------------------------*/

.progress {
    background-color: transparent;
    border: .125rem solid #f4b200;
    border-radius: 0;
    height: .625rem;
}

.progress .progress-bar {
    background-color: #f4b200;
}

/*-------------------------------------------
  -- Promo Numbers
-------------------------------------------*/

.ts-promo-numbers h2 {
    font-weight: normal;
}

.ts-promo-numbers h3 {
    font-weight: normal;
}

.ts-promo-number {
    margin-top: 1rem;
    margin-bottom: 1rem;
    position: relative;
}

.ts-promo-number .ts-promo-number-divider:after {
    content: "";
    bottom: 0;
    border: .125rem solid #f4b200;
    border-radius: 50%;
    height: .625rem;
    margin: auto;
    position: absolute;
    right: -0.3125rem;
    top: 0;
    width: .625rem;
}

/*-------------------------------------------
  -- Select
-------------------------------------------*/

select.form-control {
    box-shadow: .125rem .1875rem .9375rem rgba(0, 0, 0, .15);
    border-radius: .25rem;
    cursor: pointer;
    height: 2.8125rem !important;
    margin-top: -0.125rem;
    padding: .5rem;
    -webkit-appearance: none;
       -moz-appearance: none;
    text-indent: .0625rem;
    text-overflow: '';
}

select.form-control:focus, select.form-control:hover {
    box-shadow: .375rem .3125rem 1.5625rem rgba(0, 0, 0, .2);
}

select::-ms-expand {
    display: none;
}

.select-wrapper {
    position: relative;
}

.select-wrapper:before {
    position: absolute;
    display: inline-block;
    font-weight: 900;
    text-rendering: auto;
    top: 0;
    margin: auto;
    bottom: 0;
    right: .9375rem;
    height: 1.875rem;
    -webkit-font-smoothing: antialiased;
    font-family: "Font Awesome\ 5 Free";
    content: "\f0dd";
}

/*-------------------------------------------
  -- Slider
-------------------------------------------*/

.ts-slider {
    height: 100% !important;
}

.ts-slider div {
    height: 100% !important;
}

/*-------------------------------------------
  -- Tabs
-------------------------------------------*/

.nav-tabs {
    border-bottom: none;
}

.nav-tabs h4 {
    font-weight: normal;
    margin-bottom: 0;
}

.nav-tabs .nav-link {
    background-color: transparent;
    border: none;
    border-bottom: .1875rem solid transparent;
    margin-left: .9375rem;
    margin-right: .9375rem;
    padding-right: 0;
    padding-left: 0;
    color: inherit;
    opacity: .5;
}

.nav-tabs .nav-link.active {
    color: #191919;
    background-color: transparent;
    border-bottom: .1875rem solid #f4b200;
    opacity: 1;
}

/***********************************************************************************************************************
D. Plugins Styles
***********************************************************************************************************************/

/*-------------------------------------------
  -- Magnific Popup
-------------------------------------------*/

/* overlay at start */

.mfp-fade.mfp-bg {
    opacity: 0;
    background-color: #000;
    -webkit-transition: all .15s ease-out;
       -moz-transition: all .15s ease-out;
            transition: all .15s ease-out;
}

/* overlay animate in */

.mfp-fade.mfp-bg.mfp-ready {
    opacity: .8;
}

/* overlay animate out */

.mfp-fade.mfp-bg.mfp-removing {
    opacity: 0;
}

/* content at start */

.mfp-fade.mfp-wrap .mfp-content {
    opacity: 0;
    -webkit-transition: all .15s ease-out;
       -moz-transition: all .15s ease-out;
            transition: all .15s ease-out;
}

/* content animate it */

.mfp-fade.mfp-wrap.mfp-ready .mfp-content {
    opacity: 1;
}

/* content animate out */

.mfp-fade.mfp-wrap.mfp-removing .mfp-content {
    opacity: 0;
}

/*-------------------------------------------
  -- Owl Carousel
-------------------------------------------*/

.owl-carousel .owl-stage, .owl-carousel .owl-stage-outer,
.owl-carousel .owl-item {
    height: 100%;
}

.owl-carousel .owl-dots {
    text-align: center;
}

.owl-carousel .owl-dots .owl-dot {
    display: inline-block;
    padding: .3125rem;
}

.owl-carousel .owl-dots .owl-dot:hover span,
.owl-carousel .owl-dots .owl-dot.active span {
    opacity: .7;
}

.owl-carousel .owl-dots .owl-dot span {
    background-color: #191919;
    border-radius: 50%;
    display: inline-block;
    height: .625rem;
    opacity: .2;
    transition: .3s ease;
    width: .625rem;
}

.owl-carousel .owl-nav {
    position: absolute;
    top: -1.25rem;
    bottom: 0;
    height: 0;
    margin: auto;
    width: 100%;
}

.owl-carousel .owl-nav .owl-prev, .owl-carousel .owl-nav .owl-next {
    background-color: rgba(25, 25, 25, .6);
    border-radius: 50%;
    box-shadow: 0 .125rem .3125rem rgba(0, 0, 0, .1);
    color: #fff;
    display: inline-block;
    height: 2.5rem;
    position: absolute;
    text-align: center;
    transition: .3s ease;
    width: 2.5rem;
}

.owl-carousel .owl-nav .owl-prev:after, .owl-carousel .owl-nav .owl-next:after {
    font-family: "Font Awesome\ 5 Free";
    font-weight: 900;
    font-size: 1.375rem;
    line-height: 2.5rem;
    -webkit-font-smoothing: antialiased;
}

.owl-carousel .owl-nav .owl-prev:hover, .owl-carousel .owl-nav .owl-next:hover {
    background-color: rgba(25, 25, 25, .8);
}

.owl-carousel .owl-nav .owl-next {
    right: .3125rem;
}

.owl-carousel .owl-nav .owl-next:after {
    content: "\f105";
    margin-left: .1875rem;
}

.owl-carousel .owl-nav .owl-prev {
    left: .3125rem;
}

.owl-carousel .owl-nav .owl-prev:after {
    content: "\f104";
    margin-right: .0625rem;
}

/***********************************************************************************************************************
E. Template Specific Elements
***********************************************************************************************************************/

/*-------------------------------------------
  -- Centered Slider
-------------------------------------------*/

.ts-carousel-centered .slide {
    margin-bottom: 1rem;
    margin-top: 1rem;
    padding: 1rem;
}

.ts-carousel-centered .owl-item {
    perspective: 1000;
}

.ts-carousel-centered .owl-item .slide {
    opacity: .5;
    transition: .3s ease;
    transform: scale(.95);
}

.ts-carousel-centered .owl-item.active.center .slide {
    opacity: 1;
    transform: scale(1);
}

.ts-carousel-centered .owl-nav .owl-prev,
.ts-carousel-centered .owl-nav .owl-next {
    height: 3.75rem;
    width: 3.75rem;
}

.ts-carousel-centered .owl-nav .owl-prev:after,
.ts-carousel-centered .owl-nav .owl-next:after {
    font-size: 1.375rem;
    line-height: 3.75rem;
}

.ts-carousel-centered .owl-nav .owl-prev:hover,
.ts-carousel-centered .owl-nav .owl-next:hover {
    background-color: rgb(25, 25, 25);
}

.ts-carousel-centered .owl-nav .owl-next {
    right: 1.25rem;
}

.ts-carousel-centered .owl-nav .owl-prev {
    left: 1.25rem;
}

/*-------------------------------------------
  -- Hero Form Floated
-------------------------------------------*/

.floated {
    position: relative;
    width: 100%;
    z-index: 1;
    bottom: -1.875rem;
}

.floated form {
    position: relative;
    padding: 1.875rem 3.75rem;
}

/*-------------------------------------------
  -- Price Box
-------------------------------------------*/

.ts-price-box__promoted {
    box-shadow: .375rem .3125rem 1.5625rem rgba(0, 0, 0, .2);
    margin-top: -1.25rem;
    margin-bottom: .625rem;
    z-index: 2;
}

.ts-price-box__promoted .ts-title {
    transform: scale(1.2);
}

/*-------------------------------------------
  -- Time Line
-------------------------------------------*/

.ts-time-line__horizontal {
    padding-bottom: .625rem;
    padding-top: .625rem;
    position: relative;
    /* timeline line */
}

.ts-time-line__horizontal ul {
    padding-left: 1.875rem;
    list-style: none;
    position: relative;
}

.ts-time-line__horizontal:after {
    background-color: #474747;
    content: "";
    bottom: 6.875rem;
    height: .1875rem;
    left: 0;
    position: absolute;
    width: 100%;
}

.ts-time-line__horizontal .ts-time-line__item {
    flex: 0 0 auto;
    margin-right: 1.875rem;
    position: relative;
    width: 18.75rem;
}

.ts-time-line__horizontal .ts-time-line__item .ts-box {
    position: relative;
    /* dot */
}

.ts-time-line__horizontal .ts-time-line__item .ts-box:before {
    background-color: #474747;
    bottom: -4.375rem;
    border-radius: 100%;
    content: "";
    left: 1.6875rem;
    height: .75rem;
    position: absolute;
    width: .75rem;
}

.ts-time-line__horizontal .ts-time-line__item .ts-box {
    /*triangle*/
}

.ts-time-line__horizontal .ts-time-line__item .ts-box:after {
    border-color: #fff transparent transparent transparent;
    border-style: solid;
    border-width: .5rem .5rem 0 .5rem;
    bottom: -0.4375rem;
    content: "";
    left: 1.5625rem;
    height: 0;
    position: absolute;
    width: 0;
}

.ts-time-line__horizontal .ts-time-line__item.ts-time-line__milestone {
    width: 4.375rem;
}

.ts-time-line__horizontal .ts-time-line__item.ts-time-line__milestone .ts-box {
    background-color: #f4b200;
    color: #fff;
}

.ts-time-line__horizontal .ts-time-line__item.ts-time-line__milestone .ts-box:after {
    border-color: #f4b200 transparent transparent transparent;
}

.ts-time-line__horizontal .ts-time-line__item.ts-time-line__milestone h5 {
    writing-mode: vertical-lr;
    margin: 0;
}

.ts-time-line__horizontal .ts-time-line__item figure {
    margin-left: 1.875rem;
    margin-top: 4.6875rem;
}

.ts-time-line__horizontal .ts-time-line__item figure small {
    text-transform: uppercase;
    opacity: .4;
}

.ts-time-line__horizontal .ts-time-line__item figure small,
.ts-time-line__horizontal .ts-time-line__item figure h6 {
    font-weight: 600;
}

.ts-time-line__horizontal .owl-stage-outer {
    padding: 1rem 1rem 0 1rem;
}

.ts-time-line__horizontal .owl-stage {
    align-items: flex-end;
    display: flex;
}

.ts-time-line__horizontal .ts-sly-frame.ts-loaded > ul {
    align-items: flex-end;
    display: flex;
}

/*-------------------------------------------
  -- SVG Shapes
-------------------------------------------*/

.ts-svg {
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
    top: 0;
    z-index: -1;
    height: 100%;
    position: absolute;
    width: 100%;
    left: 0;
    margin: auto;
}

.ts-story:hover {
    color: #fff;
}

.ts-story:hover p {
    color: #fff;
}

.ts-story:hover .ts-background {
    background-color: #000 !important;
}

.ts-story:hover .ts-background-image {
    opacity: .4 !important;
}

.ts-story {
    margin-bottom: 2rem;
    padding: 14rem 2rem 2rem 2rem;
    position: relative;
}

.ts-story .ts-background, .ts-story .ts-background-image {
    transition: .3s ease;
}

.ts-story figure {
    background-color: #fff;
    color: rgba(25, 25, 25, .2);
    font-weight: 500;
    position: absolute;
    top: -0.375rem;
    left: 3rem;
    padding: 1rem;
    transform: rotate(-90deg);
    transform-origin: bottom;
}

/*-------------------------------------------
  -- Other
-------------------------------------------*/

/* Footer push up */

#ts-footer .ts-box {
    margin-top: -3.125rem;
}

.ts-tabs-presentation .tab-pane img {
    opacity: 0;
    transition: .3s ease;
    transform: translateY(1.25rem);
}

.ts-tabs-presentation .tab-pane.show.active img {
    opacity: 1;
    transform: translateY(0);
}

/* Hero navigation arrows */

#ts-hero .owl-prev, #ts-hero .owl-next {
    background-color: transparent;
    border: .125rem solid rgba(255, 255, 255, .8);
}

#ts-hero .owl-prev:after, #ts-hero .owl-next:after {
    line-height: 2.25rem;
}

/* Hero slider height */

.ts-hero-slider {
    height: 100% !important;
}

.ts-hero-slider div {
    height: 100% !important;
}

@media (min-width: 36rem) and (max-width: 47.9375rem) {
    html {
        font-size: 85%;
    }

    h1, .ts-h1 {
        font-size: 2.5rem;
    }

    h2, .ts-h2 {
        font-size: 1.625rem;
    }

    h3, .ts-h3 {
        font-size: 1.25rem;
    }

    .ts-column-count-sm-1 {
        column-count: 1;
    }

    .ts-column-count-sm-2 {
        column-count: 2;
    }

    .ts-column-count-sm-3 {
        column-count: 3;
    }

    .ts-column-count-sm-4 {
        column-count: 4;
    }

    .ts-promo-numbers h2 {
        font-size: 2.375rem;
    }
}

@media (min-width: 48rem) and (max-width: 61.9375rem) {
    html {
        font-size: 90%;
    }

    h1, .ts-h1 {
        font-size: 3rem;
    }

    h2, .ts-h2 {
        font-size: 1.875rem;
    }

    h3, .ts-h3 {
        font-size: 1.375rem;
    }

    .ts-column-count-md-1 {
        column-count: 1;
    }

    .ts-column-count-md-2 {
        column-count: 2;
    }

    .ts-column-count-md-3 {
        column-count: 3;
    }

    .ts-column-count-md-4 {
        column-count: 4;
    }

    .ts-promo-numbers h2 {
        font-size: 2.5rem;
    }
}

@media (min-width: 62rem) and (max-width: 74.9375rem) {
    html {
        font-size: 95%;
    }

    h1, .ts-h1 {
        font-size: 3.125rem;
    }

    h2, .ts-h2 {
        font-size: 2rem;
    }

    h3, .ts-h3 {
        font-size: 1.375rem;
    }

    .ts-column-count-lg-1 {
        column-count: 1;
    }

    .ts-column-count-lg-2 {
        column-count: 2;
    }

    .ts-column-count-lg-3 {
        column-count: 3;
    }

    .ts-column-count-lg-4 {
        column-count: 4;
    }

    .ts-block {
        padding-bottom: 6.25rem;
        padding-top: 6.25rem;
    }

    .ts-card__image {
        height: 12.5rem;
    }

    .ts-promo-numbers h2 {
        font-size: 2.75rem;
    }
}

@media (min-width: 75rem) {
    html {
        font-size: 100%;
    }

    h1, .ts-h1 {
        font-size: 3.5rem;
    }

    h2, .ts-h2 {
        font-size: 2.25rem;
    }

    h3, .ts-h3 {
        font-size: 1.625rem;
    }

    .ts-column-count-xl-1 {
        column-count: 1;
    }

    .ts-column-count-xl-2 {
        column-count: 2;
    }

    .ts-column-count-xl-3 {
        column-count: 3;
    }

    .ts-column-count-xl-4 {
        column-count: 4;
    }

    .ts-block {
        padding-bottom: 8.125rem;
        padding-top: 8.125rem;
    }

    .ts-card__image {
        height: 15.625rem;
    }

    .navbar.navbar-expand-xl .navbar-nav {
        align-items: center;
    }

    .navbar.navbar-expand-xl .navbar-nav .nav-link {
        padding-top: .3125rem;
        padding-bottom: .3125rem;
        border-bottom: none;
    }

    .navbar.navbar-expand-xl .ts-background {
        opacity: 0;
    }

    .ts-promo-numbers h2 {
        font-size: 3rem;
    }

    .ts-carousel-centered .owl-nav .owl-next {
        right: 5rem;
    }

    .ts-carousel-centered .owl-nav .owl-prev {
        left: 5rem;
    }

    .floated form {
        padding: 2.5rem 5rem;
    }
}

@media (max-width: 35.9375rem) {
    h1, .ts-h1 {
        margin-bottom: 1.25rem;
    }

    [class*="ts-column-count-"] {
        column-count: 1;
    }

    .ts-xs-text-center {
        text-align: center !important;
    }

    .ts-title {
        margin-bottom: 1.875rem;
    }

    .ts-promo-numbers h2 {
        font-size: 2.25rem;
    }
}

@media (min-width: 36rem) and (max-width: 61.9375rem) {
    h1, .ts-h1 {
        margin-bottom: 1.875rem;
    }

    .ts-title {
        margin-bottom: 3.125rem;
    }

    .ts-block-inside {
        padding: 2.5rem;
    }
}

@media (min-width: 62rem) {
    h1, .ts-h1 {
        margin-bottom: 2.5rem;
    }

    .ts-title {
        margin-bottom: 5rem;
    }

    .ts-block-inside {
        padding: 3.75rem;
    }

    .navbar.navbar-expand-lg .navbar-nav {
        align-items: center;
    }

    .navbar.navbar-expand-lg .navbar-nav .nav-link {
        padding-top: .3125rem;
        padding-bottom: .3125rem;
        border-bottom: none;
    }

    .navbar.navbar-expand-lg .ts-background {
        opacity: 0;
    }

    .floated {
        position: absolute;
    }
}

@media (max-width: 47.9375rem) {
    h4, .ts-h4 {
        font-size: 1.125rem;
    }
}

@media (min-width: 48rem) {
    h4, .ts-h4 {
        font-size: 1.25rem;
    }

    .navbar.navbar-expand-md .navbar-nav {
        align-items: center;
    }

    .navbar.navbar-expand-md .navbar-nav .nav-link {
        padding-top: .3125rem;
        padding-bottom: .3125rem;
        border-bottom: none;
    }

    .navbar.navbar-expand-md .ts-background {
        opacity: 0;
    }
}

@media (max-width: 61.9375rem) {
    .ts-card__image {
        height: 15.625rem;
    }
}

@media (min-width: 36rem) {
    .navbar.navbar-expand-sm .navbar-nav {
        align-items: center;
    }

    .navbar.navbar-expand-sm .navbar-nav .nav-link {
        padding-top: .3125rem;
        padding-bottom: .3125rem;
        border-bottom: none;
    }

    .navbar.navbar-expand-sm .ts-background {
        opacity: 0;
    }

    .ts-carousel-centered .owl-nav .owl-next {
        right: 2.5rem;
    }

    .ts-carousel-centered .owl-nav .owl-prev {
        left: 2.5rem;
    }
}

    </style>
</head>

<body data-spy="scroll" data-target=".navbar" class="has-loading-screen">
    <div class="ts-page-wrapper" id="page-top">
        <!--*********************************************************************************************************-->
        <!--************ HERO ***************************************************************************************-->
        <!--*********************************************************************************************************-->
        <header id="ts-hero" class="ts-full-screen ts-separate-bg-element" style="height: 700px">
            <!--HERO CONTENT ****************************************************************************************-->
            <div class="block__style opt-border" opt-id="block-background" style="
            padding: 60px 0px;
            background: url('https://i.ontraport.com/208582.aabba9597757875e8123599b50b31eab.PNG')
              center center / cover no-repeat;
          ">
                <div class="js-opt-bg-img image-background-overlay dark-color-background" style="opacity: 0.71"></div>
                <div class="container block-align--top">
                    <div class="row" style="z-index: 2">
                        <div opt-id="8" class="col s12 m12" style="padding: 0px 0px 40px">
                            <div class="col__style col__style--top opt-border" style="padding: 0px">
                                <div class="sub-row">
                                    <div class="sub-col s1">
                                        <div class="el__style el-id-9" style="
                          margin-top: 0px;
                          margin-bottom: 5px;
                          padding: 0px;
                        ">
                                            <div class="opt-element dark-color-text body-text" opt-id="9"
                                                opt-element="text" mobile-font-size="27px" mobile-line-height="34px"
                                                style="font-size: 40px; line-height: 43px">
                                                <div class="opt-text-wrapper">
                                                    <div style="text-align: center">
                                                        <b><span class="white-color-text" style="color: #fff">It's Time
                                                                To Reintroduce Yourself.<br /><span
                                                                    class="primary-color-text"
                                                                    style="color: #bf973f">Master the Art of
                                                                    Self-Reinvention.</span></span></b>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="sub-row">
                                    <div class="sub-col s1">
                                        <div class="el__style el-id-4" style="
                          margin: 22px auto 20px;
                          padding: 0px;
                          left: 0px;
                          text-align: center;
                          max-width: 97%;
                        ">
                                            <div class="opt-button__text-container" style="
                            background: linear-gradient(
                              to bottom,
                              #bf973f,
                              #fbc85f
                            );
                            color: #fff;
                            padding: 20px;
                            font-size: 20px;
                          ">
                                                <div
                                                    class="opt-button__text-target white-color-text white-color-text--hover label">
                                                    <b>CLICK HERE TO REGISTER FOR THE RECORDING</b>
                                                </div>
                                                <div
                                                    class="opt-button__sub-text-target white-color-text white-color-text--hover body-text">
                                                    YOU WILL NEED TO JOIN THE INNER CIRCLE ON THE NEXT
                                                    PAGE
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row" style="z-index: 1">
                        <div opt-id="1" class="col s12 m6" style="padding: 10px 0px">
                            <div class="col__style col__style--top opt-border" style="padding: 0px">
                                <div class="sub-row">
                                    <div class="sub-col s1 sub-col--liquid-override">
                                        <div class="el__style el-id-5" style="
                          margin-top: 20px;
                          margin-bottom: 0px;
                          padding: 0px;
                          left: 0%;
                          max-width: 96%;
                        ">
                                            <div class="opt-element opt-video video-background-wrapper z-depth-30 z-depth-30--hover opt-border complementary-color-border complementary-color-border--hover"
                                                opt-id="5" data-video-provider="vimeo">
                                                <div class="video-background-container video-background--no-transform">
                                                    <div class="video-container">
                                                        <iframe allowfullscreen=""
                                                            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                                                            src="https://player.vimeo.com/video/908128441?h=dabf2b4d1a&amp;autoplay=1&amp;loop=0"
                                                            frameborder="0"
                                                            data-src="https://player.vimeo.com/video/908128441?h=dabf2b4d1a&amp;autoplay=1&amp;loop=0"></iframe>
                                                    </div>
                                                </div>
                                                <div class="video-background-overlay video-background-overlay--normal">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div opt-id="7" class="col s12 m6">
                            <div class="col__style">
                                <div class="sub-row">
                                    <div class="sub-col s1">
                                        <div class="el__style el-id-10" style="
                          margin-top: 10px;
                          margin-bottom: 0px;
                          padding: 0px 0px 0px 30px;
                          max-width: 100%;
                        ">
                                            <div class="opt-element dark-color-text h2" opt-id="10"
                                                opt-element="sub-headline" data-font-family="'Lato', sans-serif"
                                                mobile-font-size="18px" mobile-line-height="31px" style="
                            font-family: Lato, sans-serif;
                            font-size: 27px;
                            line-height: 37px;
                          ">
                                                <div class="opt-text-wrapper">
                                                    <div style="text-align: center; color: #fff">
                                                        <span class="white-color-text"><span data-cke-bookmark="1"
                                                                style="display: none">&nbsp;</span>This is 2024
                                                            —<br />The world is changing.<br />Your
                                                            work is changing.<br />Your industry is
                                                            changing.<br />It’s time for you to learn how to
                                                            change the way you think, act and achieve.<br /><br />
                                                            <span class="primary-color-text"
                                                                style="color: #bf973f"><b>It’s Time To Learn How To
                                                                    ReInvent
                                                                    Yourself</b></span></span><br />
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="sub-row">
                                    <div class="sub-col s1">
                                        <div class="el__style el-id-13" style="
                          margin: 22px auto 20px;
                          padding: 0px;
                          left: 0px;
                          text-align: center;
                          max-width: 97%;
                        ">
                                            <div class="opt-button__text-container" style="
                            background: linear-gradient(
                              to bottom,
                              #bf973f,
                              #fbc85f
                            );
                            color: #fff;
                            padding: 20px;
                            font-size: 20px;
                          ">
                                                <div
                                                    class="opt-button__text-target white-color-text white-color-text--hover label">
                                                    <b>CLICK HERE TO REGISTER FOR THE RECORDING</b>
                                                </div>
                                                <div
                                                    class="opt-button__sub-text-target white-color-text white-color-text--hover body-text">
                                                    YOU WILL NEED TO JOIN THE INNER CIRCLE ON THE NEXT
                                                    PAGE
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!--end #hero-->

        <!--*********************************************************************************************************-->
        <!--************ CONTENT ************************************************************************************-->
        <!--*********************************************************************************************************-->
        <main id="ts-content">
            <!--LATEST COURSES **************************************************************************************-->
            <section>
                <div class="block__style opt-border" opt-id="block-background"
                    style="padding: 40px 0px; background-color: transparent">
                    <div class="js-opt-bg-img bg-color-overlay"
                        style="background-color: rgb(245, 245, 245); opacity: 1"></div>
                    <div class="container block-align--top">
                        <div class="row" style="z-index: 1">
                            <div opt-id="1" class="col s12 m12">
                                <div class="col__style">
                                    <div class="sub-row">
                                        <div class="sub-col s1">
                                            <div class="el__style el-id-2" style="
                            margin: 4px auto 10px;
                            padding: 0px;
                            left: 0px;
                            max-width: 100%;
                          ">
                                                <div class="opt-element dark-color-text h1" opt-id="2"
                                                    opt-element="headline" data-font-family="" mobile-font-size="28px"
                                                    mobile-line-height="39px"
                                                    style="font-size: 42px; line-height: 50px">
                                                    <div class="opt-text-wrapper">
                                                        <div class="opt-text-wrapper">
                                                            <div style="text-align: center">
                                                                <span style="background-color: transparent"><span
                                                                        class="dark-color-text"><span
                                                                            data-cke-bookmark="1"
                                                                            style="display: none">&nbsp;</span>Imagine<span
                                                                            data-cke-bookmark="1"
                                                                            style="display: none">&nbsp;</span></span></span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="sub-row">
                                        <div class="sub-col s1">
                                            <div class="el__style el-id-3" style="
                            margin-top: 10px;
                            margin-bottom: 0px;
                            padding: 0px 0px 0px 30px;
                            max-width: 100%;
                          ">
                                                <div class="opt-element dark-color-text h2" opt-id="3"
                                                    opt-element="sub-headline" data-font-family="'Lato', sans-serif"
                                                    mobile-font-size="19px" mobile-line-height="25px" style="
                              font-family: Lato, sans-serif;
                              font-size: 24px;
                              line-height: 40px;
                            ">
                                                    <div class="opt-text-wrapper">
                                                        <div style="text-align: center">
                                                            <span class="dark-color-text"><i><i>👉🏾&nbsp;</i></i>Waking
                                                                up in the morning feeling completely
                                                                excited about who you are BEING in the world
                                                                and what are you doing with your time.<br /><span
                                                                    class="dark-color-text"><i><i>👉🏾&nbsp;</i></i>Feeling
                                                                    that spark of passion, things that
                                                                    deeply matters to
                                                                    you</span><br /><i><i>👉🏾&nbsp;</i></i>Imagine just
                                                                being myself in every situation,
                                                                not having to put on a show for anyone.</span><br />
                                                        </div>
                                                        <div style="text-align: center">
                                                            <i><i>👉🏾&nbsp;</i></i>to have real connections with
                                                            people,
                                                            relationships where I can share my true thoughts
                                                            and feelings, and they can do the same. Genuine,
                                                            deep connections."
                                                        </div>
                                                        <div style="text-align: center">
                                                            <span class="dark-color-text">Pure, unfiltered
                                                                authenticity.<br /><br />The
                                                                only barrier standing before your next level
                                                                is YOU.</span><br />
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="sub-row">
                                        <div class="el__style el-id-4" style="
                            margin-top: 24px;
                            margin-bottom: 20px;
                            padding: 0px;
                            
                          ">
                                            <div class="opt-button__text-container" style="
                            background: linear-gradient(
                              to bottom,
                              #bf973f,
                              #fbc85f
                            );
                            color: #fff;
                            padding: 20px;
                            font-size: 20px;
                            text-align: center;
                          ">
                                                <div
                                                    class="opt-button__text-target white-color-text white-color-text--hover h2">
                                                    <b>CLICK HERE TO REGISTER FOR THE RECORDING</b>
                                                </div>
                                                <div
                                                    class="opt-button__sub-text-target white-color-text white-color-text--hover body-text">
                                                    YOU WILL NEED TO JOIN THE INNER CIRCLE ON THE
                                                    NEXT PAGE
                                                </div>
                                            </div>

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
    </div>
    </section>
    <section>
        <div class="block__style opt-border" opt-id="block-background"
            style="padding: 28px 15px; background: url('https://i.ontraport.com/208582.62b94c0b6f9e48ed12a935e41ce92738.PNG') center center / cover no-repeat;">
            <div class="js-opt-bg-img image-background-overlay dark-color-background" style="opacity: 0.34;"></div>
            <div class="container block-align--top">
                <div class="row" style="z-index: 3;">
                    <div opt-id="1" class="col s12 m12 " style="padding: 0px;">
                        <div class="col__style col__style--top opt-border" style="padding: 0px 0px 30px;">
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-6"
                                        style="margin-top: 5px; margin-bottom: 20px; padding: 0px 0px 0px 10px;">
                                        <div class="opt-element dark-color-text large-body-text" opt-id="6"
                                            opt-element="text" data-font-family="" mobile-font-size="24px"
                                            style="font-size: 41px; line-height: 53px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center" style="color: #fff !important"><span
                                                        style="color: #fff !important">What you will learn</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row" style="z-index: 2;">
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa0}</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="38" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-39"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-40"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="40"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">Deep
                                                            Thinking</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-41"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="41"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa1}</span><br></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="59" class="col s12 m4"
                        style="padding: 0px 10px;  background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent;">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-60"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-61"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="61"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">Elite
                                                            Community</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-62"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="62"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa2}</span><br></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa3}.</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa4}.</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa5}.</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa6}.</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa7}.</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa8}.</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div opt-id="33" class="col s12 m4"
                        style="padding: 0px 10px; background-color: #000; color: #fff; margin: 5px; min-width: 30%;">
                        <div class="col__style col__style--top opt-border"
                            style="padding: 20px; background-color: transparent; ">
                            <div class="js-opt-bg-img bg-color-overlay dark-color-background" style="opacity: 1;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-37"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px; text-align: center;">
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-35"
                                        style="margin-top: 10px; margin-bottom: 0px; padding: 0px;">
                                        <div class="opt-element dark-color-text h2" opt-id="35"
                                            opt-element="sub-headline">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><b><span class="white-color-text">FIRE
                                                            Training</span></b></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-36"
                                        style="margin-top: 10px; margin-bottom: 10px; padding: 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="36"
                                            opt-element="text" style="font-size: 18px; line-height: 27px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text">{pa9}.</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row" style="z-index: 1;">
                    <div opt-id="31" class="col s12 m12 " style="padding: 59px 0px 0px;">
                        <div class="col__style col__style--top opt-border" style="padding: 0px;">
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-32"
                                        style="margin: 12px auto; padding: 0px 10px; left: 0px; max-width: 75%;">
                                        <div class="opt-element dark-color-text body-text" opt-id="32"
                                            opt-element="text" data-font-family="" mobile-font-size="17px"
                                            mobile-line-height="23px" style="font-size: 23px; line-height: 31px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text"><span
                                                            style="background-color:transparent; color: #fff;">As a high
                                                            achiever, you
                                                            often hear, <span class="primary-color-text"><b>“look at how
                                                                    much you’ve already accomplished… settle
                                                                    down”</b></span><br><br><span
                                                                class="primary-color-text"><b>But you KNOW there is
                                                                    more.</b></span><br>You know there is a greater
                                                            level of significance that is available whether others want
                                                            to play at that level or not.<br><br>You are grateful for
                                                            your success but ready for
                                                            significance.</span></span><br><span
                                                        class="white-color-text"><span
                                                            style="background-color:transparent"><i></i></span></span><br>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--LATEST COURSES **************************************************************************************-->
     <section>
        <div class="block__style opt-border" opt-id="block-background" style="padding: 0px; background: transparent;">
            <div class="container full-width block-align--middle" style="max-width: 100%;">
                <div class="row" style="z-index: 1; color: #fff;">
                    <div opt-id="2" class="col s12 m7" style="padding: 0px;">
                        <div class="js-opt-bg-img image-background-color" style="background-color: transparent;"></div>
                        <div class="col__style col__style--center opt-border"
                            style="padding: 59px 178px; background: url('https://i.ontraport.com/208582.e5b1618aa09b77a29f929ccdf57df0f0.PNG') center center / cover no-repeat;">
                            <div class="js-opt-bg-img image-background-overlay dark-color-background"
                                style="opacity: 0.07;"></div>
                            <div class="sub-row">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-27"
                                        style="margin-top: 30px; margin-bottom: 15px; padding: 0px 4px;">
                                        <div class="" opt-id="27" opt-element="text" data-font-family=""
                                            mobile-font-size="18px" style="font-size: 27px; line-height: 31px;">
                                            <div class="opt-text-wrapper">
                                                <div><span class="white-color-text"><span class="dark-color-text"><span
                                                                class="primary-color-text"><b>Author introduction<span
                                                                        data-cke-bookmark="1"
                                                                        style="display:none">&nbsp;</span></b></span></span></span><br>
                                                </div>
                                                <div style="margin-left: 42px;" class="opt-text-wrapper"><span
                                                    class="white-color-text">{info}.</b></span><br></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!--END LATEST COURSES**** ******************************************************************************-->
    </main>
    <!--end #content-->

    <!--*********************************************************************************************************-->
    <!--************ FOOTER *************************************************************************************-->
    <!--*********************************************************************************************************-->
    <section id="ts-footer">
        <div class="block__style opt-border" opt-id="block-background"
            style="padding: 10px 45px; background-color: transparent;">
            <div class="js-opt-bg-img bg-color-overlay white-color-background" style="opacity: 1;"></div>
            <div class="container block-align--top">
                <div class="row" style="z-index: 1;">
                    <div opt-id="1" class="col s12 m12 " style="padding: 0px;">
                        <div class="col__style col__style--center opt-border" style="padding: 40px 0px;">
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-5"
                                        style="margin: 0px auto 10px; padding: 0px; left: 0px;">
                                        <div class="opt-element dark-color-text h1" opt-id="5" opt-element="headline"
                                            mobile-font-size="26px" mobile-line-height="43px"
                                            style="font-size: 38px; line-height: 44px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="primary-color-text"><span
                                                            class="dark-color-text">Contrary to popular belief, I did
                                                            not just work HARDER...&nbsp;</span></span><br></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-6"
                                        style="margin-top: 24px; margin-bottom: 0px; padding: 0px 0px 0px 10px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="6" opt-element="text"
                                            data-font-family="'Open Sans Condensed', sans-serif" mobile-font-size="18px"
                                            style="font-family: &quot;Open Sans Condensed&quot;, sans-serif; font-size: 22px; line-height: 34px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span><span><span><span
                                                                    style="color:#000000"><span><span><span>I committed
                                                                                to myself and my family to learn how to
                                                                                <b>LEARN</b>.<br>To change how I
                                                                                think.<br>I learned how to re-invent
                                                                                myself.</span></span></span></span></span></span></span><br>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-7"
                                        style="margin-top: 26px; margin-bottom: 20px; padding: 0px; left: 17%; max-width: 70%;">
                                        <!-- <a class="opt-element opt-button white-color-text opt-theme-hover-target op-gradient-tb-bf973f-fbc85f op-gradient-tb-bf973f-primary--hover z-depth-00 z-depth-30--hover opt-border"
                                            opt-id="7" opt-button-style-type="gradient" opt-button-icon-display="none"
                                            opt-button-width="full" opt-button-type="text" href="javascript://"
                                            target="_self" data-opf-trigger="p2c208582f56" data-url_type="ontraform"
                                            button_text_font="h2" button_sub_text_font="body-text"
                                            style="padding: 20px 10px;"
                                            data-opf-trigger-guid="OPF_9e5c30d6-1a26-2c56-7a8c-95b921982114"> <i
                                                opt-type="icon"
                                                class="opt-element material-icons white-color-text white-color-text--hover"
                                                style="font-size: 32px;">settings</i>
                                            <div class="opt-button__text-container">
                                                <div
                                                    class="opt-button__text-target white-color-text white-color-text--hover h2">
                                                    Click Here To Get The Recording</div>
                                                <div
                                                    class="opt-button__sub-text-target white-color-text white-color-text--hover body-text">
                                                    You Will Need To Join The Inner Circle On The Next Page<br></div>
                                            </div>
                                        </a></div> -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    </section>
    <section>
        <div class="block__style opt-border" opt-id="block-background"
            style="padding: 40px 0px; background: url('https://i.ontraport.com/208582.e5b1618aa09b77a29f929ccdf57df0f0.PNG') center center / cover no-repeat;">
            <div class="js-opt-bg-img image-background-overlay" style="background-color: transparent; opacity: 0;">
            </div>
            <div class="container block-align--top">
                <div class="row" style="z-index: 1;">
                    <div opt-id="1" class="col s12 m12 ">
                        <div class="col__style">
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-2"
                                        style="margin-top: 18px; margin-bottom: 10px; padding: 0px 20px;">
                                        <div class="opt-element dark-color-text body-text" opt-id="2"
                                            opt-element="headline" data-font-family="" mobile-font-family=""
                                            mobile-font-size="18px" mobile-line-height=""
                                            style="font-size: 21px; line-height: 33px;">
                                            <div class="opt-text-wrapper">
                                                <div style="text-align:center"><span class="white-color-text"><span
                                                            style="font-family:Montserrat,sans-serif; color: #fff;"><b>BECAUSE
                                                                REINVENTING YOURSELF IS NOT AN OPTION…<br>IT'S A
                                                                NECESSITY</b></span></span><br></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="sub-row ">
                                <div class="sub-col s1">
                                    <div class="el__style el-id-3"
                                        style="margin: 20px auto; padding: 0px 20px; left: 0px;">
                                        <div opt-id="3" class="opt-element opt-custom-html">
                                            <script type="text/javascript" async="true"
                                                src="https://app.ontraport.com/js/ontraport/opt_assets/drivers/opf.js"
                                                data-opf-uid="p2c208582f56"
                                                data-opf-params="borderColor=#000000&amp;borderSize=0px&amp;formHeight=1080&amp;formWidth=540px&amp;maxTriggers=2&amp;onExitIntent=true&amp;popPosition=mc&amp;timeframe=1&amp;instance=n344757945"
                                                data-_opf-register-guid="OPF_9e5c30d6-1a26-2c56-7a8c-95b921982114"></script>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!--end #footer-->
    </div>

    <script src="assets/js/custom.hero.js"></script>
    <script src="assets/js/jquery-3.3.1.min.js"></script>
    <script src="assets/js/popper.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/imagesloaded.pkgd.min.js"></script>
    <script src="http://maps.google.com/maps/api/js?key=AIzaSyBEDfNcQRmKQEyulDN8nGWjLYPm8s4YB58"></script>
    <script src="assets/js/isInViewport.jquery.js"></script>
    <script src="assets/js/jquery.magnific-popup.min.js"></script>
    <script src="assets/js/owl.carousel.min.js"></script>
    <script src="assets/js/scrolla.jquery.min.js"></script>
    <script src="assets/js/jquery.validate.min.js"></script>
    <script src="assets/js/jquery-validate.bootstrap-tooltip.min.js"></script>
    <script src="assets/js/custom.js"></script>
</body>

</html>
"""
