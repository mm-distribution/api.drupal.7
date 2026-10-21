# search_expand_cjk()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 475–499 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L475-L499)
- **Module/theme:** search

## Signature

```php
function search_expand_cjk($matches)
```

## Documentation

```text
Splits CJK (Chinese, Japanese, Korean) text into tokens.

The Search module matches exact words, where a word is defined to be a
sequence of characters delimited by spaces or punctuation. CJK languages are
written in long strings of characters, though, not split up into words. So
in order to allow search matching, we split up CJK text into tokens
consisting of consecutive, overlapping sequences of characters whose length
is equal to the 'minimum_word_size' variable. This tokenizing is only done if
the 'overlap_cjk' variable is TRUE.

@param $matches
  This function is a callback for preg_replace_callback(), which is called
  from search_simplify(). So, $matches is an array of regular expression
  matches, which means that $matches[0] contains the matched text -- a string
  of CJK characters to tokenize.

@return
  Tokenized text, starting and ending with a space character.
```

## Code

```php
function search_expand_cjk($matches) {
  $min = variable_get('minimum_word_size', 3);
  $str = $matches[0];
  $length = drupal_strlen($str);
  // If the text is shorter than the minimum word size, don't tokenize it.
  if ($length <= $min) {
    return ' ' . $str . ' ';
  }
  $tokens = ' ';
  // Build a FIFO queue of characters.
  $chars = array();
  for ($i = 0; $i < $length; $i++) {
    // Add the next character off the beginning of the string to the queue.
    $current = drupal_substr($str, 0, 1);
    $str = substr($str, strlen($current));
    $chars[] = $current;
    if ($i >= $min - 1) {
      // Make a token of $min characters, and add it to the token string.
      $tokens .= implode('', $chars) . ' ';
      // Shift out the first character in the queue.
      array_shift($chars);
    }
  }
  return $tokens;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
