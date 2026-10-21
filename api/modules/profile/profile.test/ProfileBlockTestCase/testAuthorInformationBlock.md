# ProfileBlockTestCase::testAuthorInformationBlock()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 417–469 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L417-L469)
- **Class:** [ProfileBlockTestCase](../ProfileBlockTestCase.md)
- **Module/theme:** profile

## Signature

```php
function testAuthorInformationBlock()
```

## Documentation

_No docblock in source._

## Code

```php
  function testAuthorInformationBlock() {
    // Set the block to a region to confirm the block is available.
    $edit = array();
    $edit['blocks[profile_author-information][region]'] = 'footer';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertText(t('The block settings have been updated.'), 'Block successfully move to footer region.');

    // Enable field 1.
    $this->drupalPost('admin/structure/block/manage/profile/author-information/configure', array(
      'profile_block_author_fields[' . $this->field1['form_name'] . ']' => TRUE,
    ), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block configuration set.');

    // Visit the node and confirm that the field is displayed.
    $this->drupalGet('node/' . $this->node->nid);
    $this->assertRaw($this->value1, 'Field 1 is displayed');
    $this->assertNoRaw($this->value2, 'Field 2 is not displayed');

    // Enable only field 2.
    $this->drupalPost('admin/structure/block/manage/profile/author-information/configure', array(
      'profile_block_author_fields[' . $this->field1['form_name'] . ']' => FALSE,
      'profile_block_author_fields[' . $this->field2['form_name'] . ']' => TRUE,
    ), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block configuration set.');

    // Visit the node and confirm that the field is displayed.
    $this->drupalGet('node/' . $this->node->nid);
    $this->assertNoRaw($this->value1, 'Field 1 is not displayed');
    $this->assertRaw($this->value2, 'Field 2 is displayed');

    // Enable both fields.
    $this->drupalPost('admin/structure/block/manage/profile/author-information/configure', array(
      'profile_block_author_fields[' . $this->field1['form_name'] . ']' => TRUE,
      'profile_block_author_fields[' . $this->field2['form_name'] . ']' => TRUE,
    ), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block configuration set.');

    // Visit the node and confirm that the field is displayed.
    $this->drupalGet('node/' . $this->node->nid);
    $this->assertRaw($this->value1, 'Field 1 is displayed');
    $this->assertRaw($this->value2, 'Field 2 is displayed');

    // Enable the link to the user profile.
    $this->drupalPost('admin/structure/block/manage/profile/author-information/configure', array(
      'profile_block_author_fields[user_profile]' => TRUE,
    ), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block configuration set.');

    // Visit the node and confirm that the user profile link is displayed.
    $this->drupalGet('node/' . $this->node->nid);
    $this->clickLink(t('View full user profile'));
    $this->assertEqual($this->getUrl(), url('user/' . $this->normal_user->uid, array('absolute' => TRUE)));
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
