# SearchConfigSettingsForm::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1456–1480 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1456-L1480)
- **Class:** [SearchConfigSettingsForm](../SearchConfigSettingsForm.md)
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
    parent::setUp('search', 'search_extra_type');

    // Login as a user that can create and search content.
    $this->search_user = $this->drupalCreateUser(array('search content', 'administer search', 'administer nodes', 'bypass node access', 'access user profiles', 'administer users', 'administer blocks', 'access site reports'));
    $this->drupalLogin($this->search_user);

    // Add a single piece of content and index it.
    $node = $this->drupalCreateNode();
    $this->search_node = $node;
    // Link the node to itself to test that it's only indexed once. The content
    // also needs the word "pizza" so we can use it as the search keyword.
    $langcode = LANGUAGE_NONE;
    $body_key = "body[$langcode][0][value]";
    $edit[$body_key] = l($node->title, 'node/' . $node->nid) . ' pizza sandwich';
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    node_update_index();
    search_update_totals();

    // Enable the search block.
    $edit = array();
    $edit['blocks[search_form][region]'] = 'content';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
