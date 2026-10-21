# hook_search_preprocess()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 287–290 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L287-L290)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_search_preprocess($text)
```

## Documentation

```text
Preprocess text for search.

This hook is called to preprocess both the text added to the search index and
the keywords users have submitted for searching.

Possible uses:
- Adding spaces between words of Chinese or Japanese text.
- Stemming words down to their root words to allow matches between, for
  instance, walk, walked, walking, and walks in searching.
- Expanding abbreviations and acronymns that occur in text.

@param $text
  The text to preprocess. This is a single piece of plain text extracted
  from between two HTML tags or from the search query. It will not contain
  any HTML entities or HTML tags.

@return
  The text after preprocessing. Note that if your module decides not to alter
  the text, it should return the original text. Also, after preprocessing,
  words in the text should be separated by a space.

@ingroup search
```

## Code

```php
function hook_search_preprocess($text) {
  // Do processing on $text
  return $text;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_preprocess()".

_None found._

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
