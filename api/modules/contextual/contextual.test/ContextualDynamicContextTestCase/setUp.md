# ContextualDynamicContextTestCase::setUp()

- **Type:** Method
- **File:** [`modules/contextual/contextual.test`](../_file.md), lines 22–28 · [local source](../../../../../source/modules/contextual/contextual.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.test#L22-L28)
- **Class:** [ContextualDynamicContextTestCase](../ContextualDynamicContextTestCase.md)
- **Module/theme:** contextual

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('contextual', 'node'));
    $this->drupalCreateContentType(array('type' => 'page', 'name' => 'Basic page'));
    $this->drupalCreateContentType(array('type' => 'article', 'name' => 'Article'));
    $web_user = $this->drupalCreateUser(array('access content', 'access contextual links', 'edit any article content'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/contextual/contextual.test](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.test) · Licensed GPL-2.0-or-later (see LICENSE)._
