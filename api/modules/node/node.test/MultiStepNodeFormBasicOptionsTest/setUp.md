# MultiStepNodeFormBasicOptionsTest::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2191–2195 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2191-L2195)
- **Class:** [MultiStepNodeFormBasicOptionsTest](../MultiStepNodeFormBasicOptionsTest.md)
- **Module/theme:** node

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('poll');
    $web_user = $this->drupalCreateUser(array('administer nodes', 'create poll content'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
