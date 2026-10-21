# FilterHooksTestCase::testFilterHooks()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1952–1990 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1952-L1990)
- **Class:** [FilterHooksTestCase](../FilterHooksTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFilterHooks()
```

## Documentation

```text
Tests hooks on format management.

Tests that hooks run correctly on creating, editing, and deleting a text
format.
```

## Code

```php
  function testFilterHooks() {
    // Add a text format.
    $name = $this->randomName();
    $edit = array();
    $edit['format'] = drupal_strtolower($this->randomName());
    $edit['name'] = $name;
    $edit['roles[' . DRUPAL_ANONYMOUS_RID . ']'] = 1;
    $this->drupalPost('admin/config/content/formats/add', $edit, t('Save configuration'));
    $this->assertRaw(t('Added text format %format.', array('%format' => $name)), 'New format created.');
    $this->assertText('hook_filter_format_insert invoked.', 'hook_filter_format_insert was invoked.');

    $format_id = $edit['format'];

    // Update text format.
    $edit = array();
    $edit['roles[' . DRUPAL_AUTHENTICATED_RID . ']'] = 1;
    $this->drupalPost('admin/config/content/formats/' . $format_id, $edit, t('Save configuration'));
    $this->assertRaw(t('The text format %format has been updated.', array('%format' => $name)), 'Format successfully updated.');
    $this->assertText('hook_filter_format_update invoked.', 'hook_filter_format_update() was invoked.');

    // Add a new custom block.
    $custom_block = array();
    $custom_block['info'] = $this->randomName(8);
    $custom_block['title'] = $this->randomName(8);
    $custom_block['body[value]'] = $this->randomName(32);
    // Use the format created.
    $custom_block['body[format]'] = $format_id;
    $this->drupalPost('admin/structure/block/add', $custom_block, t('Save block'));
    $this->assertText(t('The block has been created.'), 'New block successfully created.');

    // Verify the new block is in the database.
    $bid = db_query("SELECT bid FROM {block_custom} WHERE info = :info", array(':info' => $custom_block['info']))->fetchField();
    $this->assertNotNull($bid, 'New block found in database');

    // Disable the text format.
    $this->drupalPost('admin/config/content/formats/' . $format_id . '/disable', array(), t('Disable'));
    $this->assertRaw(t('Disabled text format %format.', array('%format' => $name)), 'Format successfully disabled.');
    $this->assertText('hook_filter_format_disable invoked.', 'hook_filter_format_disable() was invoked.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
