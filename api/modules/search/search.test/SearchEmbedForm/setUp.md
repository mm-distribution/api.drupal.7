# SearchEmbedForm::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1890–1906 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1890-L1906)
- **Class:** [SearchEmbedForm](../SearchEmbedForm.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('search', 'search_embedded_form');

    // Create a user and a node, and update the search index.
    $test_user = $this->drupalCreateUser(array('access content', 'search content', 'administer nodes'));
    $this->drupalLogin($test_user);

    $this->node = $this->drupalCreateNode();

    node_update_index();
    search_update_totals();

    // Set up a dummy initial count of times the form has been submitted.
    $this->submit_count = 12;
    variable_set('search_embedded_form_submitted', $this->submit_count);
    $this->refreshVariables();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
