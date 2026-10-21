# hook_mail()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2602–2638 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2602-L2638)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_mail($key, &$message, $params)
```

## Documentation

```text
Prepare a message based on parameters; called from drupal_mail().

Note that hook_mail(), unlike hook_mail_alter(), is only called on the
$module argument to drupal_mail(), not all modules.

@param $key
  An identifier of the mail.
@param $message
  An array to be filled in. Elements in this array include:
  - id: An ID to identify the mail sent. Look at module source code
    or drupal_mail() for possible id values.
  - to: The address or addresses the message will be sent to. The formatting
    of this string will be validated with the
    @link http://php.net/manual/filter.filters.validate.php PHP e-mail validation filter. @endlink
  - subject: Subject of the e-mail to be sent. This must not contain any
    newline characters, or the mail may not be sent properly. drupal_mail()
    sets this to an empty string when the hook is invoked.
  - body: An array of lines containing the message to be sent. Drupal will
    format the correct line endings for you. drupal_mail() sets this to an
    empty array when the hook is invoked.
  - from: The address the message will be marked as being from, which is
    set by drupal_mail() to either a custom address or the site-wide
    default email address when the hook is invoked.
  - headers: Associative array containing mail headers, such as From,
    Sender, MIME-Version, Content-Type, etc. drupal_mail() pre-fills
    several headers in this array.
@param $params
  An array of parameters supplied by the caller of drupal_mail().
```

## Code

```php
function hook_mail($key, &$message, $params) {
  $account = $params['account'];
  $context = $params['context'];
  $variables = array(
    '%site_name' => variable_get('site_name', 'Drupal'),
    '%username' => format_username($account),
  );
  if ($context['hook'] == 'taxonomy') {
    $entity = $params['entity'];
    $vocabulary = taxonomy_vocabulary_load($entity->vid);
    $variables += array(
      '%term_name' => $entity->name,
      '%term_description' => $entity->description,
      '%term_id' => $entity->tid,
      '%vocabulary_name' => $vocabulary->name,
      '%vocabulary_description' => $vocabulary->description,
      '%vocabulary_id' => $vocabulary->vid,
    );
  }

  // Node-based variable translation is only available if we have a node.
  if (isset($params['node'])) {
    $node = $params['node'];
    $variables += array(
      '%uid' => $node->uid,
      '%node_url' => url('node/' . $node->nid, array('absolute' => TRUE)),
      '%node_type' => node_type_get_name($node),
      '%title' => $node->title,
      '%teaser' => $node->teaser,
      '%body' => $node->body,
    );
  }
  $subject = strtr($context['subject'], $variables);
  $body = strtr($context['message'], $variables);
  $message['subject'] .= str_replace(array("\r", "\n"), '', $subject);
  $message['body'][] = drupal_html_to_text($body);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_mail()".

- [contact_mail()](../../contact/contact.module/contact_mail.md) — `modules/contact/contact.module`
- [system_mail()](../system.module/system_mail.md) — `modules/system/system.module`
- [update_mail()](../../update/update.module/update_mail.md) — `modules/update/update.module`
- [user_mail()](../../user/user.module/user_mail.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
