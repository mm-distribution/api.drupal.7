# TaxonomyTermTestCase::testTermAutocompletion()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 756–803 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L756-L803)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTermAutocompletion()
```

## Documentation

```text
Tests term autocompletion edge cases with slashes in the names.
```

## Code

```php
  function testTermAutocompletion() {
    // Add a term with a slash in the name.
    $first_term = $this->createTerm($this->vocabulary);
    $first_term->name = '10/16/2011';
    taxonomy_term_save($first_term);
    // Add another term that differs after the slash character.
    $second_term = $this->createTerm($this->vocabulary);
    $second_term->name = '10/17/2011';
    taxonomy_term_save($second_term);
    // Add another term that has both a comma and a slash character.
    $third_term = $this->createTerm($this->vocabulary);
    $third_term->name = 'term with, a comma and / a slash';
    taxonomy_term_save($third_term);

    // Try to autocomplete a term name that matches both terms.
    // We should get both term in a json encoded string.
    $input = '10/';
    $path = 'taxonomy/autocomplete/taxonomy_';
    $path .= $this->vocabulary->machine_name . '/' . $input;
    // The result order is not guaranteed, so check each term separately.
    $url = url($path, array('absolute' => TRUE));
    $result = drupal_http_request($url);
    $data = drupal_json_decode($result->data);
    $this->assertEqual($data[$first_term->name], check_plain($first_term->name), 'Autocomplete returned the first matching term.');
    $this->assertEqual($data[$second_term->name], check_plain($second_term->name), 'Autocomplete returned the second matching term.');

    // Try to autocomplete a term name that matches first term.
    // We should only get the first term in a json encoded string.
    $input = '10/16';
    $url = 'taxonomy/autocomplete/taxonomy_';
    $url .= $this->vocabulary->machine_name . '/' . $input;
    $this->drupalGet($url);
    $target = array($first_term->name => check_plain($first_term->name));
    $this->assertRaw(drupal_json_encode($target), 'Autocomplete returns only the expected matching term.');

    // Try to autocomplete a term name with both a comma and a slash.
    $input = '"term with, comma and / a';
    $url = 'taxonomy/autocomplete/taxonomy_';
    $url .= $this->vocabulary->machine_name . '/' . $input;
    $this->drupalGet($url);
    $n = $third_term->name;
    // Term names containing commas or quotes must be wrapped in quotes.
    if (strpos($third_term->name, ',') !== FALSE || strpos($third_term->name, '"') !== FALSE) {
      $n = '"' . str_replace('"', '""', $third_term->name) . '"';
    }
    $target = array($n => check_plain($third_term->name));
    $this->assertRaw(drupal_json_encode($target), 'Autocomplete returns a term containing a comma and a slash.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
