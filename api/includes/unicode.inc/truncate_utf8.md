# truncate_utf8()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 321–365 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L321-L365)

## Signature

```php
function truncate_utf8($string, $max_length, $wordsafe = FALSE, $add_ellipsis = FALSE, $min_wordsafe_length = 1)
```

## Documentation

```text
Truncates a UTF-8-encoded string safely to a number of characters.

@param $string
  The string to truncate.
@param $max_length
  An upper limit on the returned string length, including trailing ellipsis
  if $add_ellipsis is TRUE.
@param $wordsafe
  If TRUE, attempt to truncate on a word boundary. Word boundaries are
  spaces, punctuation, and Unicode characters used as word boundaries in
  non-Latin languages; see PREG_CLASS_UNICODE_WORD_BOUNDARY for more
  information. If a word boundary cannot be found that would make the length
  of the returned string fall within length guidelines (see parameters
  $max_length and $min_wordsafe_length), word boundaries are ignored.
@param $add_ellipsis
  If TRUE, add t('...') to the end of the truncated string (defaults to
  FALSE). The string length will still fall within $max_length.
@param $min_wordsafe_length
  If $wordsafe is TRUE, the minimum acceptable length for truncation (before
  adding an ellipsis, if $add_ellipsis is TRUE). Has no effect if $wordsafe
  is FALSE. This can be used to prevent having a very short resulting string
  that will not be understandable. For instance, if you are truncating the
  string "See myverylongurlexample.com for more information" to a word-safe
  return length of 20, the only available word boundary within 20 characters
  is after the word "See", which wouldn't leave a very informative string. If
  you had set $min_wordsafe_length to 10, though, the function would realise
  that "See" alone is too short, and would then just truncate ignoring word
  boundaries, giving you "See myverylongurl..." (assuming you had set
  $add_ellipses to TRUE).

@return string
  The truncated string.
```

## Code

```php
function truncate_utf8($string, $max_length, $wordsafe = FALSE, $add_ellipsis = FALSE, $min_wordsafe_length = 1) {
  $ellipsis = '';
  $max_length = max($max_length, 0);
  $min_wordsafe_length = max($min_wordsafe_length, 0);

  if (drupal_strlen($string) <= $max_length) {
    // No truncation needed, so don't add ellipsis, just return.
    return $string;
  }

  if ($add_ellipsis) {
    // Truncate ellipsis in case $max_length is small.
    $ellipsis = drupal_substr(t('...'), 0, $max_length);
    $max_length -= drupal_strlen($ellipsis);
    $max_length = max($max_length, 0);
  }

  if ($max_length <= $min_wordsafe_length) {
    // Do not attempt word-safe if lengths are bad.
    $wordsafe = FALSE;
  }

  if ($wordsafe) {
    $matches = array();
    // Find the last word boundary, if there is one within $min_wordsafe_length
    // to $max_length characters. preg_match() is always greedy, so it will
    // find the longest string possible.
    $found = preg_match('/^(.{' . $min_wordsafe_length . ',' . $max_length . '})[' . PREG_CLASS_UNICODE_WORD_BOUNDARY . ']/u', $string, $matches);
    if ($found) {
      $string = $matches[1];
    }
    else {
      $string = drupal_substr($string, 0, $max_length);
    }
  }
  else {
    $string = drupal_substr($string, 0, $max_length);
  }

  if ($add_ellipsis) {
    $string .= $ellipsis;
  }

  return $string;
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
