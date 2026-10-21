# TranslationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 16–22 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L16-L22)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Translation functionality',
      'description' => 'Create a basic page with translation, modify the page outdating translation, and update translation.',
      'group' => 'Translation'
    );
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
