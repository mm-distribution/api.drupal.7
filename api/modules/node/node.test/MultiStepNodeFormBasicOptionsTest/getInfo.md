# MultiStepNodeFormBasicOptionsTest::getInfo()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2183–2189 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2183-L2189)
- **Class:** [MultiStepNodeFormBasicOptionsTest](../MultiStepNodeFormBasicOptionsTest.md)
- **Module/theme:** node

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
      'name' => 'Multistep node form basic options',
      'description' => 'Test the persistence of basic options through multiple steps.',
      'group' => 'Node',
    );
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
