# -*- coding: utf-8 -*-
"""
    pygments.styles.perldoc
    ~~~~~~~~~~~~~~~~~~~~~~~

    Style similar to the style used in the `perldoc`_ code blocks.

    .. _perldoc: http://perldoc.perl.org/

    :copyright: 2006 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic


class PerldocStyle(Style):

    background_color = '#eeeedd'
    default_style = ''

    styles = {
        Comment:                '#228B22',
        Comment.Preproc:        '#1e889b',

        String:                 '#CD5555',
        String.Heredoc:         '#1c7e71 italic',
        String.Regex:           '#B452CD',
        String.Other:           '#cb6c20',
        String.Regex:           '#1c7e71',

        Number:                 '#B452CD',

        Operator.Word:          '#8B008B',

        Keyword:                '#8B008B bold',
        Keyword.Type:           '#a7a7a7',

        Name.Class:             '#008b45 bold',
        Name.Exception:         '#008b45 bold',
        Name.Function:          '#008b45',
        Name.Namespace:         '#008b45 underline',
        Name.Variable:          '#00688B',
        Name.Constant:          '#00688B',
        Name.Decorator:         '#707a7c',
        Name.Tag:               '#8B008B bold',
        Name.Attribute:         '#658b00',
        Name.Builtin:           '#658b00',

        Generic.Heading:        'bold #000080',
        Generic.Subheading:     'bold #800080',
        Generic.Deleted:        '#aa0000',
        Generic.Inserted:       '#00aa00',
        Generic.Error:          '#aa0000',
        Generic.Emph:           'italic',
        Generic.Strong:         'bold',
        Generic.Prompt:         '#555555',
        Generic.Output:         '#888888',
        Generic.Traceback:      '#aa0000',

        Error:                  'bg:#e3d2d2 #a61717'
    }
