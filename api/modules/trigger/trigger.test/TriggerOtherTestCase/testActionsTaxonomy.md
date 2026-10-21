# TriggerOtherTestCase::testActionsTaxonomy()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 652–683 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L652-L683)
- **Class:** [TriggerOtherTestCase](../TriggerOtherTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testActionsTaxonomy()
```

## Documentation

```text
Tests triggering on taxonomy new term.
```

## Code

```php
  function testActionsTaxonomy() {
    // Assign an action to the taxonomy term save trigger.
    $test_user = $this->drupalCreateUser(array('administer actions'));
    $this->drupalLogin($test_user);
    $action_id = 'trigger_test_generic_action';
    $hash = drupal_hash_base64($action_id);
    $edit = array('aid' => $hash);
    $this->drupalPost('admin/structure/trigger/taxonomy', $edit, t('Assign'), array(), array(), 'trigger-taxonomy-term-insert-assign-form');

    // Set action variable to FALSE.
    variable_set($action_id, FALSE);

    // Create a taxonomy vocabulary and add a term to it.

    // Create a vocabulary.
    $vocabulary = new stdClass();
    $vocabulary->name = $this->randomName();
    $vocabulary->description = $this->randomName();
    $vocabulary->machine_name = drupal_strtolower($this->randomName());
    $vocabulary->help = '';
    $vocabulary->nodes = array('article' => 'article');
    $vocabulary->weight = mt_rand(0, 10);
    taxonomy_vocabulary_save($vocabulary);

    $term = new stdClass();
    $term->name = $this->randomName();
    $term->vid = $vocabulary->vid;
    taxonomy_term_save($term);

    // Verify that the action variable has been set.
    $this->assertTrue(variable_get($action_id, FALSE), 'Check that creating a taxonomy term triggered the action.');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
