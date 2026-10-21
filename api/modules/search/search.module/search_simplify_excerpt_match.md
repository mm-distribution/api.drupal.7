# search_simplify_excerpt_match()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1291–1337 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1291-L1337)
- **Module/theme:** search

## Signature

```php
function search_simplify_excerpt_match($key, $text, $offset, $boundary)
```

## Documentation

```text
Find words in the original text that matched via search_simplify().

This is called in search_excerpt() if an exact match is not found in the
text, so that we can find the derived form that matches.

@param $key
  The keyword to find.
@param $text
  The text to search for the keyword.
@param $offset
  Offset position in $text to start searching at.
@param $boundary
  Text to include in a regular expression that will match a word boundary.

@return
  FALSE if no match is found. If a match is found, return an associative
  array with element 'where' giving the position of the match, and element
  'keyword' giving the actual word found in the text at that position.
```

## Code

```php
function search_simplify_excerpt_match($key, $text, $offset, $boundary) {
  $pos = NULL;
  $simplified_key = search_simplify($key);
  $simplified_text = search_simplify($text);

  // Return immediately if simplified key or text are empty.
  if (!$simplified_key || !$simplified_text) {
    return FALSE;
  }

  // Check if we have a match after simplification in the text.
  if (!preg_match('/' . $boundary . $simplified_key . $boundary . '/iu', $simplified_text, $match, PREG_OFFSET_CAPTURE, $offset)) {
    return FALSE;
  }

  // If we get here, we have a match. Now find the exact location of the match
  // and the original text that matched. Start by splitting up the text by all
  // potential starting points of the matching text and iterating through them.
  $split = array_filter(preg_split('/' . $boundary . '/iu', $text, -1, PREG_SPLIT_OFFSET_CAPTURE), '_search_excerpt_match_filter');
  foreach ($split as $value) {
    // Skip starting points before the offset.
    if ($value[1] < $offset) {
      continue;
    }

    // Check a window of 80 characters after the starting point for a match,
    // based on the size of the excerpt window.
    $window = substr($text, $value[1], 80);
    $simplified_window = search_simplify($window);
    if (strpos($simplified_window, $simplified_key) === 0) {
      // We have a match in this window. Store the position of the match.
      $pos = $value[1];
      // Iterate through the text in the window until we find the full original
      // matching text.
      $length = strlen($window);
      for ($i = 1; $i <= $length; $i++) {
        $keyfound = substr($text, $value[1], $i);
        if ($simplified_key == search_simplify($keyfound)) {
          break;
        }
      }
      break;
    }
  }

  return $pos ? array('where' => $pos, 'keyword' => $keyfound) : FALSE;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
