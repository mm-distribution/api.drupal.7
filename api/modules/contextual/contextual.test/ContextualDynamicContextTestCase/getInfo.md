# ContextualDynamicContextTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/contextual/contextual.test`](../_file.md), lines 14–20 · [local source](../../../../../source/modules/contextual/contextual.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.test#L14-L20)
- **Class:** [ContextualDynamicContextTestCase](../ContextualDynamicContextTestCase.md)
- **Module/theme:** contextual

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
      'name' => 'Contextual links on node lists',
      'description' => 'Tests if contextual links are showing on the front page depending on permissions.',
      'group' => 'Contextual',
    );
  }
```

---
_Drupal 7.103 · [modules/contextual/contextual.test](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.test) · Licensed GPL-2.0-or-later (see LICENSE)._
