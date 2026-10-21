# RdfTrackerAttributesTestCase::setUp()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 589–598 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L589-L598)
- **Class:** [RdfTrackerAttributesTestCase](../RdfTrackerAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('rdf', 'rdf_test', 'tracker');
    // Enable anonymous posting of content.
    user_role_change_permissions(DRUPAL_ANONYMOUS_RID, array(
      'create article content' => TRUE,
      'access comments' => TRUE,
      'post comments' => TRUE,
      'skip comment approval' => TRUE,
    ));
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
