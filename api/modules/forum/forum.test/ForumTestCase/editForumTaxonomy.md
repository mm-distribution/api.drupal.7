# ForumTestCase::editForumTaxonomy()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 364–397 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L364-L397)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
function editForumTaxonomy()
```

## Documentation

```text
Edits the forum taxonomy.
```

## Code

```php
  function editForumTaxonomy() {
    // Backup forum taxonomy.
    $vid = variable_get('forum_nav_vocabulary', '');
    $original_settings = taxonomy_vocabulary_load($vid);

    // Generate a random name/description.
    $title = $this->randomName(10);
    $description = $this->randomName(100);

    $edit = array(
      'name' => $title,
      'description' => $description,
      'machine_name' => drupal_strtolower(drupal_substr($this->randomName(), 3, 9)),
    );

    // Edit the vocabulary.
    $this->drupalPost('admin/structure/taxonomy/' . $original_settings->machine_name . '/edit', $edit, t('Save'));
    $this->assertResponse(200);
    $this->assertRaw(t('Updated vocabulary %name.', array('%name' => $title)), 'Vocabulary was edited');

    // Grab the newly edited vocabulary.
    entity_get_controller('taxonomy_vocabulary')->resetCache();
    $current_settings = taxonomy_vocabulary_load($vid);

    // Make sure we actually edited the vocabulary properly.
    $this->assertEqual($current_settings->name, $title, 'The name was updated');
    $this->assertEqual($current_settings->description, $description, 'The description was updated');

    // Restore the original vocabulary.
    taxonomy_vocabulary_save($original_settings);
    drupal_static_reset('taxonomy_vocabulary_load');
    $current_settings = taxonomy_vocabulary_load($vid);
    $this->assertEqual($current_settings->name, $original_settings->name, 'The original vocabulary settings were restored');
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
