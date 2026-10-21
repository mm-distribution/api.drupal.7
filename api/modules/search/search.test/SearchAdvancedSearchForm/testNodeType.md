# SearchAdvancedSearchForm::testNodeType()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 350–376 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L350-L376)
- **Class:** [SearchAdvancedSearchForm](../SearchAdvancedSearchForm.md)
- **Module/theme:** search

## Signature

```php
function testNodeType()
```

## Documentation

```text
Test using the search form with GET and POST queries.
Test using the advanced search form to limit search to nodes of type "Basic page".
```

## Code

```php
  function testNodeType() {
    $this->assertTrue($this->node->type == 'page', 'Node type is Basic page.');

    // Assert that the dummy title doesn't equal the real title.
    $dummy_title = 'Lorem ipsum';
    $this->assertNotEqual($dummy_title, $this->node->title, "Dummy title doesn't equal node title");

    // Search for the dummy title with a GET query.
    $this->drupalGet('search/node/' . $dummy_title);
    $this->assertNoText($this->node->title, 'Basic page node is not found with dummy title.');

    // Search for the title of the node with a GET query.
    $this->drupalGet('search/node/' . $this->node->title);
    $this->assertText($this->node->title, 'Basic page node is found with GET query.');

    // Search for the title of the node with a POST query.
    $edit = array('or' => $this->node->title);
    $this->drupalPost('search/node', $edit, t('Advanced search'));
    $this->assertText($this->node->title, 'Basic page node is found with POST query.');

    // Advanced search type option.
    $this->drupalPost('search/node', array_merge($edit, array('type[page]' => 'page')), t('Advanced search'));
    $this->assertText($this->node->title, 'Basic page node is found with POST query and type:page.');

    $this->drupalPost('search/node', array_merge($edit, array('type[article]' => 'article')), t('Advanced search'));
    $this->assertText('bike shed', 'Article node is not found with POST query and type:article.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
