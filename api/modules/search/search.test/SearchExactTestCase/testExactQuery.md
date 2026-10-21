# SearchExactTestCase::testExactQuery()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 709–748 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L709-L748)
- **Class:** [SearchExactTestCase](../SearchExactTestCase.md)
- **Module/theme:** search

## Signature

```php
function testExactQuery()
```

## Documentation

```text
Tests that the correct number of pager links are found for both keywords and phrases.
```

## Code

```php
  function testExactQuery() {
    // Login with sufficient privileges.
    $this->drupalLogin($this->drupalCreateUser(array('create page content', 'search content')));

    $settings = array(
      'type' => 'page',
      'title' => 'Simple Node',
    );
    // Create nodes with exact phrase.
    for ($i = 0; $i <= 17; $i++) {
      $settings['body'] = array(LANGUAGE_NONE => array(array('value' => 'love pizza')));
      $this->drupalCreateNode($settings);
    }
    // Create nodes containing keywords.
    for ($i = 0; $i <= 17; $i++) {
      $settings['body'] = array(LANGUAGE_NONE => array(array('value' => 'love cheesy pizza')));
      $this->drupalCreateNode($settings);
    }

    // Update the search index.
    module_invoke_all('update_index');
    search_update_totals();

    // Refresh variables after the treatment.
    $this->refreshVariables();

    // Test that the correct number of pager links are found for keyword search.
    $edit = array('keys' => 'love pizza');
    $this->drupalPost('search/node', $edit, t('Search'));
    $this->assertLinkByHref('page=1', 0, '2nd page link is found for keyword search.');
    $this->assertLinkByHref('page=2', 0, '3rd page link is found for keyword search.');
    $this->assertLinkByHref('page=3', 0, '4th page link is found for keyword search.');
    $this->assertNoLinkByHref('page=4', '5th page link is not found for keyword search.');

    // Test that the correct number of pager links are found for exact phrase search.
    $edit = array('keys' => '"love pizza"');
    $this->drupalPost('search/node', $edit, t('Search'));
    $this->assertLinkByHref('page=1', 0, '2nd page link is found for exact phrase search.');
    $this->assertNoLinkByHref('page=2', '3rd page link is not found for exact phrase search.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
