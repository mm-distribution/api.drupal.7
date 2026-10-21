# FilterFormatAccessTestCase::testFormatWidgetPermissions()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 616–727 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L616-L727)
- **Class:** [FilterFormatAccessTestCase](../FilterFormatAccessTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFormatWidgetPermissions()
```

## Documentation

```text
Tests editing a page using a disallowed text format.

Verifies that regular users and administrators are able to edit a page, but
not allowed to change the fields which use an inaccessible text format.
Also verifies that fields which use a text format that does not exist can
be edited by administrators only, but that the administrator is forced to
choose a new format before saving the page.
```

## Code

```php
  function testFormatWidgetPermissions() {
    $langcode = LANGUAGE_NONE;
    $title_key = "title";
    $body_value_key = "body[$langcode][0][value]";
    $body_format_key = "body[$langcode][0][format]";

    // Create node to edit.
    $this->drupalLogin($this->admin_user);
    $edit = array();
    $edit['title'] = $this->randomName(8);
    $edit[$body_value_key] = $this->randomName(16);
    $edit[$body_format_key] = $this->disallowed_format->format;
    $this->drupalPost('node/add/page', $edit, t('Save'));
    $node = $this->drupalGetNodeByTitle($edit['title']);

    // Try to edit with a less privileged user.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('node/' . $node->nid);
    $this->clickLink(t('Edit'));

    // Verify that body field is read-only and contains replacement value.
    $this->assertFieldByXPath("//textarea[@name='$body_value_key' and @disabled='disabled']", t('This field has been disabled because you do not have sufficient permissions to edit it.'), 'Text format access denied message found.');

    // Verify that title can be changed, but preview displays original body.
    $new_edit = array();
    $new_edit['title'] = $this->randomName(8);
    $this->drupalPost(NULL, $new_edit, t('Preview'));
    $this->assertText($edit[$body_value_key], 'Old body found in preview.');

    // Save and verify that only the title was changed.
    $this->drupalPost(NULL, $new_edit, t('Save'));
    $this->assertNoText($edit['title'], 'Old title not found.');
    $this->assertText($new_edit['title'], 'New title found.');
    $this->assertText($edit[$body_value_key], 'Old body found.');

    // Check that even an administrator with "administer filters" permission
    // cannot edit the body field if they do not have specific permission to
    // use its stored format. (This must be disallowed so that the
    // administrator is never forced to switch the text format to something
    // else.)
    $this->drupalLogin($this->filter_admin_user);
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertFieldByXPath("//textarea[@name='$body_value_key' and @disabled='disabled']", t('This field has been disabled because you do not have sufficient permissions to edit it.'), 'Text format access denied message found.');

    // Disable the text format used above.
    filter_format_disable($this->disallowed_format);
    $this->resetFilterCaches();

    // Log back in as the less privileged user and verify that the body field
    // is still disabled, since the less privileged user should not be able to
    // edit content that does not have an assigned format.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertFieldByXPath("//textarea[@name='$body_value_key' and @disabled='disabled']", t('This field has been disabled because you do not have sufficient permissions to edit it.'), 'Text format access denied message found.');

    // Log back in as the filter administrator and verify that the body field
    // can be edited.
    $this->drupalLogin($this->filter_admin_user);
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertNoFieldByXPath("//textarea[@name='$body_value_key' and @disabled='disabled']", NULL, 'Text format access denied message not found.');
    $this->assertFieldByXPath("//select[@name='$body_format_key']", NULL, 'Text format selector found.');

    // Verify that trying to save the node without selecting a new text format
    // produces an error message, and does not result in the node being saved.
    $old_title = $new_edit['title'];
    $new_title = $this->randomName(8);
    $edit = array('title' => $new_title);
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertText(t('!name field is required.', array('!name' => t('Text format'))), 'Error message is displayed.');
    $this->drupalGet('node/' . $node->nid);
    $this->assertText($old_title, 'Old title found.');
    $this->assertNoText($new_title, 'New title not found.');

    // Now select a new text format and make sure the node can be saved.
    $edit[$body_format_key] = filter_fallback_format();
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertUrl('node/' . $node->nid);
    $this->assertText($new_title, 'New title found.');
    $this->assertNoText($old_title, 'Old title not found.');

    // Switch the text format to a new one, then disable that format and all
    // other formats on the site (leaving only the fallback format).
    $this->drupalLogin($this->admin_user);
    $edit = array($body_format_key => $this->allowed_format->format);
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertUrl('node/' . $node->nid);
    foreach (filter_formats() as $format) {
      if ($format->format != filter_fallback_format()) {
        filter_format_disable($format);
      }
    }

    // Since there is now only one available text format, the widget for
    // selecting a text format would normally not display when the content is
    // edited. However, we need to verify that the filter administrator still
    // is forced to make a conscious choice to reassign the text to a different
    // format.
    $this->drupalLogin($this->filter_admin_user);
    $old_title = $new_title;
    $new_title = $this->randomName(8);
    $edit = array('title' => $new_title);
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertText(t('!name field is required.', array('!name' => t('Text format'))), 'Error message is displayed.');
    $this->drupalGet('node/' . $node->nid);
    $this->assertText($old_title, 'Old title found.');
    $this->assertNoText($new_title, 'New title not found.');
    $edit[$body_format_key] = filter_fallback_format();
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertUrl('node/' . $node->nid);
    $this->assertText($new_title, 'New title found.');
    $this->assertNoText($old_title, 'Old title not found.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
