# TaxonomyTokenReplaceTestCase::testTaxonomyTokenReplacement()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1894–2001 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1894-L2001)
- **Class:** [TaxonomyTokenReplaceTestCase](../TaxonomyTokenReplaceTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTokenReplacement()
```

## Documentation

```text
Creates some terms and a node, then tests the tokens generated from them.
```

## Code

```php
  function testTaxonomyTokenReplacement() {
    global $language;

    // Create two taxonomy terms.
    $term1 = $this->createTerm($this->vocabulary);
    $term2 = $this->createTerm($this->vocabulary);

    // Edit $term2, setting $term1 as parent.
    $edit = array();
    $edit['name'] = '<blink>Blinking Text</blink>';
    $edit['parent[]'] = array($term1->tid);
    $this->drupalPost('taxonomy/term/' . $term2->tid . '/edit', $edit, t('Save'));

    // Create node with term2.
    $edit = array();
    $node = $this->drupalCreateNode(array('type' => 'article'));
    $edit[$this->instance['field_name'] . '[' . $this->langcode . '][]'] = $term2->tid;
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    // Generate and test sanitized tokens for term1.
    $tests = array();
    $tests['[term:tid]'] = $term1->tid;
    $tests['[term:name]'] = check_plain($term1->name);
    $tests['[term:description]'] = check_markup($term1->description, $term1->format);
    $tests['[term:url]'] = url('taxonomy/term/' . $term1->tid, array('absolute' => TRUE));
    $tests['[term:node-count]'] = 0;
    $tests['[term:parent:name]'] = '[term:parent:name]';
    $tests['[term:vocabulary:name]'] = check_plain($this->vocabulary->name);

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('term' => $term1), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized taxonomy term token %token replaced.', array('%token' => $input)));
    }

    // Generate and test sanitized tokens for term2.
    $tests = array();
    $tests['[term:tid]'] = $term2->tid;
    $tests['[term:name]'] = check_plain($term2->name);
    $tests['[term:description]'] = check_markup($term2->description, $term2->format);
    $tests['[term:url]'] = url('taxonomy/term/' . $term2->tid, array('absolute' => TRUE));
    $tests['[term:node-count]'] = 1;
    $tests['[term:parent:name]'] = check_plain($term1->name);
    $tests['[term:parent:url]'] = url('taxonomy/term/' . $term1->tid, array('absolute' => TRUE));
    $tests['[term:parent:parent:name]'] = '[term:parent:parent:name]';
    $tests['[term:vocabulary:name]'] = check_plain($this->vocabulary->name);

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('term' => $term2), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized taxonomy term token %token replaced.', array('%token' => $input)));
    }

    // Generate and test unsanitized tokens.
    $tests['[term:name]'] = $term2->name;
    $tests['[term:description]'] = $term2->description;
    $tests['[term:parent:name]'] = $term1->name;
    $tests['[term:vocabulary:name]'] = $this->vocabulary->name;

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('term' => $term2), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized taxonomy term token %token replaced.', array('%token' => $input)));
    }

    // Generate and test sanitized tokens.
    $tests = array();
    $tests['[vocabulary:vid]'] = $this->vocabulary->vid;
    $tests['[vocabulary:name]'] = check_plain($this->vocabulary->name);
    $tests['[vocabulary:description]'] = filter_xss($this->vocabulary->description);
    $tests['[vocabulary:node-count]'] = 1;
    $tests['[vocabulary:term-count]'] = 2;

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('vocabulary' => $this->vocabulary), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized taxonomy vocabulary token %token replaced.', array('%token' => $input)));
    }

    // Generate and test unsanitized tokens.
    $tests['[vocabulary:name]'] = $this->vocabulary->name;
    $tests['[vocabulary:description]'] = $this->vocabulary->description;

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('vocabulary' => $this->vocabulary), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized taxonomy vocabulary token %token replaced.', array('%token' => $input)));
    }

    // Verify that tokens are generated for terms with empty description.
    $term1->description = '';
    taxonomy_term_save($term1);
    $term2->description = NULL;
    taxonomy_term_save($term2);

    // Generate and test sanitized tokens.
    $tests = array();
    $tests['[term:description]'] = '';

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('term' => $term1), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized taxonomy term token %token replaced.', array('%token' => $input)));

      $output = token_replace($input, array('term' => $term2), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized taxonomy term token %token replaced.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
