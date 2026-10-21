# FilterSecurityTestCase::testDisableFilterModule()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 859–884 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L859-L884)
- **Class:** [FilterSecurityTestCase](../FilterSecurityTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testDisableFilterModule()
```

## Documentation

```text
Tests removal of filtered content when an active filter is disabled.

Tests that filtered content is emptied when an actively used filter module
is disabled.
```

## Code

```php
  function testDisableFilterModule() {
    // Create a new node.
    $node = $this->drupalCreateNode(array('promote' => 1));
    $body_raw = $node->body[LANGUAGE_NONE][0]['value'];
    $format_id = $node->body[LANGUAGE_NONE][0]['format'];
    $this->drupalGet('node/' . $node->nid);
    $this->assertText($body_raw, 'Node body found.');

    // Enable the filter_test_replace filter.
    $edit = array(
      'filters[filter_test_replace][status]' => 1,
    );
    $this->drupalPost('admin/config/content/formats/' . $format_id, $edit, t('Save configuration'));

    // Verify that filter_test_replace filter replaced the content.
    $this->drupalGet('node/' . $node->nid);
    $this->assertNoText($body_raw, 'Node body not found.');
    $this->assertText('Filter: Testing filter', 'Testing filter output found.');

    // Disable the text format entirely.
    $this->drupalPost('admin/config/content/formats/' . $format_id . '/disable', array(), t('Disable'));

    // Verify that the content is empty, because the text format does not exist.
    $this->drupalGet('node/' . $node->nid);
    $this->assertNoText($body_raw, 'Node body not found.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
