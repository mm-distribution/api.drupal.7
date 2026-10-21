# Authorized operations

- **Topic id:** `authorize`
- **Defined in:** [`modules/system/system.module`](../modules/system/system.module/_file.md), line 1731 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1731)

## Documentation

```text
@defgroup authorize Authorized operations
@{
Functions to run operations with elevated privileges via authorize.php.

Because of the Update manager functionality included in Drupal core, there
is a mechanism for running operations with elevated file system privileges,
the top-level authorize.php script. This script runs at a reduced Drupal
bootstrap level so that it is not reliant on the entire site being
functional. The operations use a FileTransfer class to manipulate code
installed on the system as the user that owns the files, not the user that
the httpd is running as.

The first setup is to define a callback function that should be authorized
to run with the elevated privileges. This callback should take a
FileTransfer as its first argument, although you can define an array of
other arguments it should be invoked with. The callback should be placed in
a separate .inc file that will be included by authorize.php.

To run the operation, certain data must be saved into the SESSION, and then
the flow of control should be redirected to the authorize.php script. There
are two ways to do this, either to call system_authorized_run() directly,
or to call system_authorized_init() and then redirect to authorize.php,
using the URL from system_authorized_get_url(). Redirecting yourself is
necessary when your authorized operation is being triggered by a form
submit handler, since calling drupal_goto() in a submit handler is a bad
idea, and you should instead set $form_state['redirect'].

Once the SESSION is setup for the operation and the user is redirected to
authorize.php, they will be prompted for their connection credentials (core
provides FTP and SSH by default, although other connection classes can be
added via contributed modules). With valid credentials, authorize.php will
instantiate the appropriate FileTransfer object, and then invoke the
desired operation passing in that object. The authorize.php script can act
as a Batch API processing page, if the operation requires a batch.

@see authorize.php
@see FileTransfer
@see hook_filetransfer_info()
```

## Members (derived, 5)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [system_authorized_batch_process()](../modules/system/system.module/system_authorized_batch_process.md) (function) — Use authorize.php to run batch_process().
- [system_authorized_batch_processing_url()](../modules/system/system.module/system_authorized_batch_processing_url.md) (function) — Returns the URL for the authorize.php script when it is processing a batch.
- [system_authorized_get_url()](../modules/system/system.module/system_authorized_get_url.md) (function) — Return the URL for the authorize.php script.
- [system_authorized_init()](../modules/system/system.module/system_authorized_init.md) (function) — Setup a given callback to run via authorize.php with elevated privileges.
- [system_authorized_run()](../modules/system/system.module/system_authorized_run.md) (function) — Setup and invoke an operation using authorize.php.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
