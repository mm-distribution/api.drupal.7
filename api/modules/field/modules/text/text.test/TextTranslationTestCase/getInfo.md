# TextTranslationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 434–440 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L434-L440)
- **Class:** [TextTranslationTestCase](../TextTranslationTestCase.md)
- **Module/theme:** text

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
      'name' => 'Text translation',
      'description' => 'Check if the text field is correctly prepared for translation.',
      'group' => 'Field types',
    );
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
