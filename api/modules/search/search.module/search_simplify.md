# search_simplify()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 411–453 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L411-L453)
- **Module/theme:** search

## Signature

```php
function search_simplify($text)
```

## Documentation

```text
Simplifies a string according to indexing rules.

@param $text
  Text to simplify.

@return
  Simplified text.

@see hook_search_preprocess()
```

## Code

```php
function search_simplify($text) {
  // Decode entities to UTF-8
  $text = decode_entities($text);

  // Lowercase
  $text = drupal_strtolower($text);

  // Call an external processor for word handling.
  search_invoke_preprocess($text);

  // Simple CJK handling
  if (variable_get('overlap_cjk', TRUE)) {
    $text = preg_replace_callback('/[' . PREG_CLASS_CJK . ']+/u', 'search_expand_cjk', $text);
  }

  // To improve searching for numerical data such as dates, IP addresses
  // or version numbers, we consider a group of numerical characters
  // separated only by punctuation characters to be one piece.
  // This also means that searching for e.g. '20/03/1984' also returns
  // results with '20-03-1984' in them.
  // Readable regexp: ([number]+)[punctuation]+(?=[number])
  $text = preg_replace('/([' . PREG_CLASS_NUMBERS . ']+)[' . PREG_CLASS_PUNCTUATION . ']+(?=[' . PREG_CLASS_NUMBERS . '])/u', '\1', $text);

  // Multiple dot and dash groups are word boundaries and replaced with space.
  // No need to use the unicode modifer here because 0-127 ASCII characters
  // can't match higher UTF-8 characters as the leftmost bit of those are 1.
  $text = preg_replace('/[.-]{2,}/', ' ', $text);

  // The dot, underscore and dash are simply removed. This allows meaningful
  // search behavior with acronyms and URLs. See unicode note directly above.
  $text = preg_replace('/[._-]+/', '', $text);

  // With the exception of the rules above, we consider all punctuation,
  // marks, spacers, etc, to be a word boundary.
  $text = preg_replace('/[' . PREG_CLASS_UNICODE_WORD_BOUNDARY . ']+/u', ' ', $text);

  // Truncate everything to 50 characters.
  $words = explode(' ', $text);
  array_walk($words, '_search_index_truncate');
  $text = implode(' ', $words);

  return $text;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
