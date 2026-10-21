# DrupalWebTestCase::drupalCreateNode()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1044–1100 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1044-L1100)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalCreateNode($settings = array())
```

## Documentation

```text
Creates a node based on default settings.

@param $settings
  An associative array of settings to change from the defaults, keys are
  node properties, for example 'title' => 'Hello, world!'.
@return
  Created node object.
```

## Code

```php
  protected function drupalCreateNode($settings = array()) {
    // Populate defaults array.
    $settings += array(
      'title'     => $this->randomName(8),
      'comment'   => 2,
      'changed'   => REQUEST_TIME,
      'moderate'  => 0,
      'promote'   => 0,
      'revision'  => 1,
      'log'       => '',
      'status'    => 1,
      'sticky'    => 0,
      'type'      => 'page',
      'revisions' => NULL,
      'language'  => LANGUAGE_NONE,
    );

    // Add the body after the language is defined so that it may be set
    // properly.
    $settings += array(
      'body' => array($settings['language'] => array(array())),
    );

    // Use the original node's created time for existing nodes.
    if (isset($settings['created']) && !isset($settings['date'])) {
      $settings['date'] = format_date($settings['created'], 'custom', 'Y-m-d H:i:s O');
    }

    // If the node's user uid is not specified manually, use the currently
    // logged in user if available, or else the user running the test.
    if (!isset($settings['uid'])) {
      if ($this->loggedInUser) {
        $settings['uid'] = $this->loggedInUser->uid;
      }
      else {
        global $user;
        $settings['uid'] = $user->uid;
      }
    }

    // Merge body field value and format separately.
    $body = array(
      'value' => $this->randomName(32),
      'format' => filter_default_format(),
    );
    $settings['body'][$settings['language']][0] += $body;

    $node = (object) $settings;
    node_save($node);

    // Small hack to link revisions to our test user.
    db_update('node_revision')
      ->fields(array('uid' => $node->uid))
      ->condition('vid', $node->vid)
      ->execute();
    return $node;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
