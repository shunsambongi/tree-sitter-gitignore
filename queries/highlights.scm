(comment) @comment
(negation) @keyword.operator

(directory_separator) @punctuation.delimiter
(directory_separator_escaped) @punctuation.delimiter

[
  (wildcard_chars)
  (wildcard_chars_allow_slash)
  (wildcard_char_single)
] @string.special

[
  (pattern_char_escaped)
  (bracket_char_escaped)
] @string.escape

(bracket_negation) @keyword.operator
(bracket_char) @character
(bracket_range) @string.special

(pattern_chars) @string
