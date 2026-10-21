# drupal_mail_system()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 269–298 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L269-L298)

## Signature

```php
function drupal_mail_system($module, $key)
```

## Documentation

```text
Returns an object that implements the MailSystemInterface interface.

Allows for one or more custom mail backends to format and send mail messages
composed using drupal_mail().

An implementation needs to implement the following methods:
- format: Allows to preprocess, format, and postprocess a mail
  message before it is passed to the sending system. By default, all messages
  may contain HTML and are converted to plain-text by the DefaultMailSystem
  implementation. For example, an alternative implementation could override
  the default implementation and additionally sanitize the HTML for usage in
  a MIME-encoded e-mail, but still invoking the DefaultMailSystem
  implementation to generate an alternate plain-text version for sending.
- mail: Sends a message through a custom mail sending engine.
  By default, all messages are sent via PHP's mail() function by the
  DefaultMailSystem implementation.

The selection of a particular implementation is controlled via the variable
'mail_system', which is a keyed array.  The default implementation
is the class whose name is the value of 'default-system' key. A more specific
match first to key and then to module will be used in preference to the
default. To specify a different class for all mail sent by one module, set
the class name as the value for the key corresponding to the module name. To
specify a class for a particular message sent by one module, set the class
name as the value for the array key that is the message id, which is
"${module}_${key}".

For example to debug all mail sent by the user module by logging it to a
file, you might set the variable as something like:

@code
array(
  'default-system' => 'DefaultMailSystem',
  'user' => 'DevelMailLog',
);
@endcode

Finally, a different system can be specified for a specific e-mail ID (see
the $key param), such as one of the keys used by the contact module:

@code
array(
  'default-system' => 'DefaultMailSystem',
  'user' => 'DevelMailLog',
  'contact_page_autoreply' => 'DrupalDevNullMailSend',
);
@endcode

Other possible uses for system include a mail-sending class that actually
sends (or duplicates) each message to SMS, Twitter, instant message, etc, or
a class that queues up a large number of messages for more efficient bulk
sending or for sending via a remote gateway so as to reduce the load
on the local server.

@param $module
  The module name which was used by drupal_mail() to invoke hook_mail().
@param $key
  A key to identify the e-mail sent. The final e-mail ID for the e-mail
  alter hook in drupal_mail() would have been {$module}_{$key}.

@return MailSystemInterface
```

## Code

```php
function drupal_mail_system($module, $key) {
  $instances = &drupal_static(__FUNCTION__, array());

  $id = $module . '_' . $key;

  $configuration = variable_get('mail_system', array('default-system' => 'DefaultMailSystem'));

  // Look for overrides for the default class, starting from the most specific
  // id, and falling back to the module name.
  if (isset($configuration[$id])) {
    $class = $configuration[$id];
  }
  elseif (isset($configuration[$module])) {
    $class = $configuration[$module];
  }
  else {
    $class = $configuration['default-system'];
  }

  if (empty($instances[$class])) {
    $interfaces = class_implements($class);
    if (isset($interfaces['MailSystemInterface'])) {
      $instances[$class] = new $class();
    }
    else {
      throw new Exception(t('Class %class does not implement interface %interface', array('%class' => $class, '%interface' => 'MailSystemInterface')));
    }
  }
  return $instances[$class];
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
