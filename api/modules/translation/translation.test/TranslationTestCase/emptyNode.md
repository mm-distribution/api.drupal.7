# TranslationTestCase::emptyNode()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 276–278 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L276-L278)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function emptyNode($langcode)
```

## Documentation

```text
Returns an empty node data structure.

@param $langcode
  The language code.

@return
  An empty node data structure.
```

## Code

```php
  function emptyNode($langcode) {
    return (object) array('nid' => NULL, 'language' => $langcode);
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
