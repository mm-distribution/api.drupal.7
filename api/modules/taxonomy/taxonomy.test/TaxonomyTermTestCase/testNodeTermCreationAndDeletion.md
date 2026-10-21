# TaxonomyTermTestCase::testNodeTermCreationAndDeletion()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 658–751 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L658-L751)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testNodeTermCreationAndDeletion()
```

## Documentation

```text
Test term creation with a free-tagging vocabulary from the node form.
```

## Code

```php
  function testNodeTermCreationAndDeletion() {
    // Enable tags in the vocabulary.
    $instance = $this->instance;
    $instance['widget'] = array('type' => 'taxonomy_autocomplete');
    $instance['bundle'] = 'page';
    field_create_instance($instance);
    // Prefix the terms with a letter to ensure there is no clash in the first
    // three letters.
    // @see https://www.drupal.org/node/2397691
    $terms = array(
      'term1' => 'a' . $this->randomName(),
      'term2' => 'b' . $this->randomName() . ', ' . $this->randomName(),
      'term3' => 'c' . $this->randomName(),
    );

    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName();
    $edit["body[$langcode][0][value]"] = $this->randomName();
    // Insert the terms in a comma separated list. Vocabulary 1 is a
    // free-tagging field created by the default profile.
    $edit[$instance['field_name'] . "[$langcode]"] = drupal_implode_tags($terms);

    // Preview and verify the terms appear but are not created.
    $this->drupalPost('node/add/page', $edit, t('Preview'));
    foreach ($terms as $term) {
      $this->assertText($term, 'The term appears on the node preview.');
    }
    $tree = taxonomy_get_tree($this->vocabulary->vid);
    $this->assertTrue(empty($tree), 'The terms are not created on preview.');

    // taxonomy.module does not maintain its static caches.
    drupal_static_reset();

    // Save, creating the terms.
    $this->drupalPost('node/add/page', $edit, t('Save'));
    $this->assertRaw(t('@type %title has been created.', array('@type' => t('Basic page'), '%title' => $edit["title"])), 'The node was created successfully.');
    foreach ($terms as $term) {
      $this->assertText($term, 'The term was saved and appears on the node page.');
    }

    // Get the created terms.
    $term_objects = array();
    foreach ($terms as $key => $term) {
      $term_objects[$key] = taxonomy_get_term_by_name($term);
      $term_objects[$key] = reset($term_objects[$key]);
    }

    // Test editing the node.
    $node = $this->drupalGetNodeByTitle($edit["title"]);
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    foreach ($terms as $term) {
      $this->assertText($term, 'The term was retained after edit and still appears on the node page.');
    }

    // Delete term 1.
    $this->drupalPost('taxonomy/term/' . $term_objects['term1']->tid . '/edit', array(), t('Delete'));
    $this->drupalPost(NULL, NULL, t('Delete'));
    $term_names = array($term_objects['term2']->name, $term_objects['term3']->name);

    // Get the node and verify that the terms that should be there still are.
    $this->drupalGet('node/' . $node->nid);
    foreach ($term_names as $term_name) {
      $this->assertText($term_name, format_string('The term %name appears on the node page after one term %deleted was deleted', array('%name' => $term_name, '%deleted' => $term_objects['term1']->name)));
    }
    $this->assertNoText($term_objects['term1']->name, format_string('The deleted term %name does not appear on the node page.', array('%name' => $term_objects['term1']->name)));

    // Test autocomplete on term 2, which contains a comma.
    // The term will be quoted, and the " will be encoded in unicode (\u0022).
    $input = substr($term_objects['term2']->name, 0, 3);
    $this->drupalGet('taxonomy/autocomplete/taxonomy_' . $this->vocabulary->machine_name . '/' . $input);
    $this->assertRaw('{"\u0022' . $term_objects['term2']->name . '\u0022":"' . $term_objects['term2']->name . '"}', format_string('Autocomplete returns term %term_name after typing the first 3 letters.', array('%term_name' => $term_objects['term2']->name)));

    // Test autocomplete on term 3 - it is alphanumeric only, so no extra
    // quoting.
    $input = substr($term_objects['term3']->name, 0, 3);
    $this->drupalGet('taxonomy/autocomplete/taxonomy_' . $this->vocabulary->machine_name . '/' . $input);
    $this->assertRaw('{"' . $term_objects['term3']->name . '":"' . $term_objects['term3']->name . '"}', format_string('Autocomplete returns term %term_name after typing the first 3 letters.', array('%term_name' => $term_objects['term3']->name)));

    // Test taxonomy autocomplete with a nonexistent field.
    $field_name = $this->randomName();
    $tag = $this->randomName();
    $message = t("Taxonomy field @field_name not found.", array('@field_name' => $field_name));
    $this->assertFalse(field_info_field($field_name), format_string('Field %field_name does not exist.', array('%field_name' => $field_name)));
    $this->drupalGet('taxonomy/autocomplete/' . $field_name . '/' . $tag);
    $this->assertRaw($message, 'Autocomplete returns correct error message when the taxonomy field does not exist.');

    // Test the autocomplete path without passing a field_name and terms.
    // This should not trigger a PHP notice.
    $field_name = '';
    $message = t("Taxonomy field @field_name not found.", array('@field_name' => $field_name));
    $this->drupalGet('taxonomy/autocomplete');
    $this->assertRaw($message, 'Autocomplete returns correct error message when no taxonomy field is given.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
