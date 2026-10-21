# CommentUninstallTestCase::testCommentUninstall()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2401–2438 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2401-L2438)
- **Class:** [CommentUninstallTestCase](../CommentUninstallTestCase.md)
- **Module/theme:** comment

## Signature

```php
function testCommentUninstall()
```

## Documentation

_No docblock in source._

## Code

```php
  function testCommentUninstall() {
    $this->drupalLogin($this->super_user);

    // Disable comment module.
    $edit['modules[Core][comment][enable]'] = FALSE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'Comment module was disabled.');

    // Uninstall comment module.
    $edit = array('uninstall[comment]' => 'comment');
    $this->drupalPost('admin/modules/uninstall', $edit, t('Uninstall'));
    $this->drupalPost(NULL, NULL, t('Uninstall'));
    $this->assertText(t('The selected modules have been uninstalled.'), 'Comment module was uninstalled.');

    // Run cron and clear field cache so that comment fields and instances
    // marked for deletion are actually removed.
    $this->cronRun();
    field_cache_clear();

    // Verify that comment fields have been removed.
    $all_fields = array_keys(field_info_field_map());
    $this->assertFalse(in_array('comment_body', $all_fields), 'Comment fields were removed by uninstall.');

    // Verify that comment field instances have been removed (or at least marked
    // for deletion).
    // N.B. field_read_instances does an INNER JOIN on field_config so if the
    // comment_body row has been removed successfully from there no instances
    // will be returned, but that does not guarantee that no rows are left over
    // in the field_config_instance table.
    $count = db_select('field_config_instance', 'fci')
      ->condition('entity_type', 'comment')
      ->condition('field_name', 'comment_body')
      ->condition('deleted', 0)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertTrue($count == 0, 'Comment field instances were removed by uninstall.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
