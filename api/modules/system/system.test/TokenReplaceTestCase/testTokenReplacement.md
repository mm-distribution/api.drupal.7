# TokenReplaceTestCase::testTokenReplacement()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2222–2266 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2222-L2266)
- **Class:** [TokenReplaceTestCase](../TokenReplaceTestCase.md)
- **Module/theme:** system

## Signature

```php
function testTokenReplacement()
```

## Documentation

```text
Creates a user and a node, then tests the tokens generated from them.
```

## Code

```php
  function testTokenReplacement() {
    // Create the initial objects.
    $account = $this->drupalCreateUser();
    $node = $this->drupalCreateNode(array('uid' => $account->uid));
    $node->title = '<blink>Blinking Text</blink>';
    global $user, $language;

    $source  = '[node:title]';         // Title of the node we passed in
    $source .= '[node:author:name]';   // Node author's name
    $source .= '[node:created:since]'; // Time since the node was created
    $source .= '[current-user:name]';  // Current user's name
    $source .= '[date:short]';         // Short date format of REQUEST_TIME
    $source .= '[user:name]';          // No user passed in, should be untouched
    $source .= '[bogus:token]';        // Non-existent token

    $target  = check_plain($node->title);
    $target .= check_plain($account->name);
    $target .= format_interval(REQUEST_TIME - $node->created, 2, $language->language);
    $target .= check_plain($user->name);
    $target .= format_date(REQUEST_TIME, 'short', '', NULL, $language->language);

    // Test that the clear parameter cleans out non-existent tokens.
    $result = token_replace($source, array('node' => $node), array('language' => $language, 'clear' => TRUE));
    $result = $this->assertEqual($target, $result, 'Valid tokens replaced while invalid tokens cleared out.');

    // Test without using the clear parameter (non-existent token untouched).
    $target .= '[user:name]';
    $target .= '[bogus:token]';
    $result = token_replace($source, array('node' => $node), array('language' => $language));
    $this->assertEqual($target, $result, 'Valid tokens replaced while invalid tokens ignored.');

    // Check that the results of token_generate are sanitized properly. This does NOT
    // test the cleanliness of every token -- just that the $sanitize flag is being
    // passed properly through the call stack and being handled correctly by a 'known'
    // token, [node:title].
    $raw_tokens = array('title' => '[node:title]');
    $generated = token_generate('node', $raw_tokens, array('node' => $node));
    $this->assertEqual($generated['[node:title]'], check_plain($node->title), 'Token sanitized.');

    $generated = token_generate('node', $raw_tokens, array('node' => $node), array('sanitize' => FALSE));
    $this->assertEqual($generated['[node:title]'], $node->title, 'Unsanitized token generated properly.');

    // Test token replacement when the string contains no tokens.
    $this->assertEqual(token_replace('No tokens here.'), 'No tokens here.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
