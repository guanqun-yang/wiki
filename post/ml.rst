================
Machine Learning
================

:Author: Guanqun Yang


.. role:: raw-latex(raw)
   :format: latex
..

Preface
=======

The following notes come from three major sources

-  School course: This is the most important source of information,
   without which I probably still do random search in a *nearly*
   infinite "learning space". Each of these courses marks the milestone
   of my experiences of doing machine learning

   #. CM 146: Introduction to Machine Learning

      This is an introductory course of machine learning and it helps me
      build up a mental repo of numerous algorithms. Just as many other
      introductory courses, an algorithm-by-algorithm style teaching is
      used by instroctor.
   #. STAT 202A: Statistical Computing

      The computation and statistical side of machine learning is the
      emphasis, both of which are largely negelected even in advanced
      level courses. The instroctor, Prof. Ying-Nian Wu, could dive into
      low level computation or jump into very high level theoretical
      generalization in a snap. These insights are invaluable for me to
      organize my mental repo previously built.
   #. CS 260: Machine Learning Algorithms

      This is the course that answers some fundamental yet negelected
      questions like "why machine could learn" and "how well machine
      could learn". Even though it is a little mathematical intensive,
      the course equips me with a full set of tools to analyze machine
      learning algorithms in a structural fashion.

-  Self-study: The self-study of machine learning started from undergrad
   when I spent a lot of time doing mathematical modeling contests. Even
   though mathematical modeling is a *totally different* perspective to
   solve problems compared with machine learning, those experiences did
   get me exposed to some terms like neural network and SVM.

   Self-study never stops ever since then but now it becomes more
   productive with help of formal education I received.
-  Project experiences: Though this may not seem to be directly releated
   to this set of notes, doing projects for project-based course or
   Kaggle let me know the power of machine learning and motivated me to
   learn more, either from school courses or self-study.

Since most of the following sections will talk about specific
algorithms, they will be organized in a similar layout and common
components may inlucde ``Motivation``, ``Algorithm``, ``Discussion`` and
``Computation``. However, when discussing learning theory, such layouts
will not be followed. :raw-latex:`\\`

Learning Theory
===============

Introduction
------------

Just like :math:`(\epsilon,\delta)` definition of limit in calculus,
learning theory tries to answer the fundamental questions like "why
machine could learn" and therefore it serves as the very foundation of
machine learning.

However, before we foremerly proceed to the details of theory or
algorithms, I think it is important to see the **distinctions** between
*learning from statistical side* and *learning from machine learning
side*, which is referred to as two different cultures in some literature
(see
`StackExchange <https://stats.stackexchange.com/questions/6/the-two-cultures-statistics-vs-machine-learning>`__).

The first viewpoint
~~~~~~~~~~~~~~~~~~~

The author of *All of Statistics*, Larry Wasserman, believes (see `his
blog
post <https://normaldeviate.wordpress.com/2012/06/12/statistics-versus-machine-learning-5-2/>`__)
there are **intrinsicly no** differences between two fields since they
both involve the process of learning from data but there **does exists**
some research perferences in each community, specifically

-  Statistic emphasizes formal statistical *inference* (confindence
   intervals, hypothesis tests, optimal easimators) in low dimensional
   problems. Some topics of interests include survival analysis time
   series, spatial analysis.
-  Machine learning emphasizes high dimensional *prediction* problems.
   Some topics of interests include online learning, semi-supervisied
   learning, manifold learning, active learning and boosting.

He also provided a table to show that seemingly different terms actually
mean the same thing (note this table is the combination of his blog post
and a table provided in his book *All of Statistics*).

.. table:: Terminology used in statistics and machine learning community

   ============================ ====================
   Statistics                   Machine Learning
   ============================ ====================
   estsimation                  learning
   classification/regression    supervisied learning
   clustering                   unpervisied learning
   classifier                   hypothesis
   data                         example/instance
   covariate                    feature
   response                     label
   frequentist inference        N/A
   Bayesian inference           Bayesian inference
   directed acyclic graph (DAG) Bayesian net
   large deviation bounds       PAC learning
   hypothesis                   N/A
   confidence interval          N/A
   ============================ ====================

*Frequentist inference* and *Bayesian inference* are again two schools
of thoughts in statistics, a dialogue-like post to show their
differences could be found
`here <https://stats.stackexchange.com/a/73180/191779>`__ (really
interesting read).

The second viewpoint
~~~~~~~~~~~~~~~~~~~~

*Learning from Data* (Yaser S. Abu-Mostafa et.al.), a book that takes a
different approach than many other machine learning books and provides a
lot of insights for me, shows the differences not only between
statistics and machine learning, but also *learning in data mining*,
specifically

-  Statistics shares the basic premises of learning from data, namely
   the use of a set of observations to uncover an underlying process. …
   . Because statistics is a mathematical field, emphasis is given to
   situations where most of the questions can be answered with rigorous
   proofs. As a result, statistis focuses on somewhat idealized models
   and analyzes them in great detail. … .Therefore, we end up with
   weaker results that are nonetheless boradly applicable.
-  Data mining is a practical field that focuses on finding patterns,
   correlations, or anomalies in large relational database. … .
   Technically, data mining is the same as learning from data, with more
   emphasis on data analysis than on prediction.

The third viewpoint
~~~~~~~~~~~~~~~~~~~

Summary of some answers on
`StackExchange <https://stats.stackexchange.com/questions/6/the-two-cultures-statistics-vs-machine-learning>`__:

-  `Answer
   1 <https://stats.stackexchange.com/questions/6/the-two-cultures-statistics-vs-machine-learning>`__

   #. Statistics papers are overwhelmingly formal and deductive while
      machine learning papers might not have proofs when proposing new
      approaches.
   #. Statistics still covers topics like survey design, sampling, which
      are of little concern for machine learning
   #. Machine learning progresses more quickly than statistics since
      their papers are generally published on conferences.

-  `Answer
   2 <https://stats.stackexchange.com/questions/6/the-two-cultures-statistics-vs-machine-learning>`__

   Statistics emphasizes *inference* of data generation process while
   machine learning emphasizes *prediction* of new data with respect to
   some variables.

:raw-latex:`\\`

Linear Regression
=================

:raw-latex:`\\`

Logistic Regression
===================
