# BlockTemplateSuggestionsUnitTest::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 719–725 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L719-L725)
- **Class:** [BlockTemplateSuggestionsUnitTest](../BlockTemplateSuggestionsUnitTest.md)
- **Module/theme:** block

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
      'name' => 'Block template suggestions',
      'description' => 'Test the template_preprocess_block() function.',
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
