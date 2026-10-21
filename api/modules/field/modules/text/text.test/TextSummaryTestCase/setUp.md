# TextSummaryTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 253–256 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L253-L256)
- **Class:** [TextSummaryTestCase](../TextSummaryTestCase.md)
- **Module/theme:** text

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    $this->article_creator = $this->drupalCreateUser(array('create article content', 'edit own article content'));
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
