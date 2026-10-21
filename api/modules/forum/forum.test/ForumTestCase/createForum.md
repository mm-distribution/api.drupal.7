# ForumTestCase::createForum()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 411–439 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L411-L439)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
function createForum($type, $parent = 0)
```

## Documentation

```text
Creates a forum container or a forum.

@param $type
  The forum type (forum container or forum).
@param $parent
  The forum parent. This defaults to 0, indicating a root forum.
  another forum).

@return
  The created taxonomy term data.
```

## Code

```php
  function createForum($type, $parent = 0) {
    // Generate a random name/description.
    $name = $this->randomName(10);
    $description = $this->randomName(100);

    $edit = array(
      'name' => $name,
      'description' => $description,
      'parent[0]' => $parent,
      'weight' => '0',
    );

    // Create forum.
    $this->drupalPost('admin/structure/forum/add/' . $type, $edit, t('Save'));
    $this->assertResponse(200);
    $type = ($type == 'container') ? 'forum container' : 'forum';
    $this->assertRaw(t('Created new @type %term.', array('%term' => $name, '@type' => t($type))), format_string('@type was created', array('@type' => ucfirst($type))));

    // Verify forum.
    $term = db_query("SELECT * FROM {taxonomy_term_data} t WHERE t.vid = :vid AND t.name = :name AND t.description = :desc", array(':vid' => variable_get('forum_nav_vocabulary', ''), ':name' => $name, ':desc' => $description))->fetchAssoc();
    $this->assertTrue(!empty($term), 'The ' . $type . ' exists in the database');

    // Verify forum hierarchy.
    $tid = $term['tid'];
    $parent_tid = db_query("SELECT t.parent FROM {taxonomy_term_hierarchy} t WHERE t.tid = :tid", array(':tid' => $tid))->fetchField();
    $this->assertTrue($parent == $parent_tid, 'The ' . $type . ' is linked to its container');

    return $term;
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
