# RenderElementTypesTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 463–469 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L463-L469)
- **Class:** [RenderElementTypesTestCase](../RenderElementTypesTestCase.md)
- **Module/theme:** batch_test

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
      'name' => 'Render element types',
      'description' => 'Tests the markup of core render element types passed to drupal_render().',
      'group' => 'Theme',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
