# NodeTokenReplaceTestCase::testNodeTokenReplacement()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2537–2646 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2537-L2646)
- **Class:** [NodeTokenReplaceTestCase](../NodeTokenReplaceTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTokenReplacement()
```

## Documentation

```text
Creates a node, then tests the tokens generated from it.
```

## Code

```php
  function testNodeTokenReplacement() {
    global $language;
    $url_options = array(
      'absolute' => TRUE,
      'language' => $language,
    );

    // Create a user and a node.
    $account = $this->drupalCreateUser();
    $settings = array(
      'type' => 'article',
      'uid' => $account->uid,
      'title' => '<blink>Blinking Text</blink>',
      'body' => array(LANGUAGE_NONE => array(array('value' => $this->randomName(32), 'summary' => $this->randomName(16)))),
    );
    $node = $this->drupalCreateNode($settings);

    // Load node so that the body and summary fields are structured properly.
    $node = node_load($node->nid);
    $instance = field_info_instance('node', 'body', $node->type);

    // Generate and test sanitized tokens.
    $tests = array();
    $langcode = entity_language('node', $node);
    $tests['[node:nid]'] = $node->nid;
    $tests['[node:vid]'] = $node->vid;
    $tests['[node:tnid]'] = $node->tnid;
    $tests['[node:type]'] = 'article';
    $tests['[node:type-name]'] = 'Article';
    $tests['[node:title]'] = check_plain($node->title);
    $tests['[node:body]'] = _text_sanitize($instance, $langcode, $node->body[$langcode][0], 'value');
    $tests['[node:summary]'] = _text_sanitize($instance, $langcode, $node->body[$langcode][0], 'summary');
    $tests['[node:language]'] = check_plain($langcode);
    $tests['[node:url]'] = url('node/' . $node->nid, $url_options);
    $tests['[node:edit-url]'] = url('node/' . $node->nid . '/edit', $url_options);
    $tests['[node:author]'] = check_plain(format_username($account));
    $tests['[node:author:uid]'] = $node->uid;
    $tests['[node:author:name]'] = check_plain(format_username($account));
    $tests['[node:created:since]'] = format_interval(REQUEST_TIME - $node->created, 2, $language->language);
    $tests['[node:changed:since]'] = format_interval(REQUEST_TIME - $node->changed, 2, $language->language);

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('node' => $node), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized node token %token replaced.', array('%token' => $input)));
    }

    // Test if the node without nid gets correct tokens (e.g. unsaved node).
    $new_node_without_nid = clone $node;
    unset($new_node_without_nid->nid);

    // Update tokens values which should be empty
    $tests['[node:nid]'] = '';
    $tests['[node:url]'] = '';
    $tests['[node:edit-url]'] = '';

    // Generate and test sanitized tokens.
    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('node' => $new_node_without_nid), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized node token %token replaced.', array('%token' => $input)));
    }

    // Revert tokens values
    $tests['[node:nid]'] = $node->nid;
    $tests['[node:url]'] = url('node/' . $node->nid, $url_options);
    $tests['[node:edit-url]'] = url('node/' . $node->nid . '/edit', $url_options);

    // Generate and test unsanitized tokens.
    $tests['[node:title]'] = $node->title;
    $tests['[node:body]'] = $node->body[$langcode][0]['value'];
    $tests['[node:summary]'] = $node->body[$langcode][0]['summary'];
    $tests['[node:language]'] = $langcode;
    $tests['[node:author:name]'] = format_username($account);

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('node' => $node), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized node token %token replaced.', array('%token' => $input)));
    }

    // Repeat for a node without a summary.
    $settings['body'] = array(LANGUAGE_NONE => array(array('value' => $this->randomName(32), 'summary' => '')));
    $node = $this->drupalCreateNode($settings);

    // Load node (without summary) so that the body and summary fields are
    // structured properly.
    $node = node_load($node->nid);
    $instance = field_info_instance('node', 'body', $node->type);

    // Generate and test sanitized token - use full body as expected value.
    $tests = array();
    $tests['[node:summary]'] = _text_sanitize($instance, $langcode, $node->body[$langcode][0], 'value');

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated for node without a summary.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('node' => $node), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized node token %token replaced for node without a summary.', array('%token' => $input)));
    }

    // Generate and test unsanitized tokens.
    $tests['[node:summary]'] = $node->body[$langcode][0]['value'];

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('node' => $node), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized node token %token replaced for node without a summary.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
