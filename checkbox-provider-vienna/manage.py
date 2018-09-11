#!/usr/bin/env python3
from plainbox.provider_manager import setup, N_

setup(
    name='checkbox-provider-vienna',
    namespace='com.canonical.qa.vienna',
    version="0.1",
    description=N_(
        "Checkbox Provider for QA of devices in the Vienna project"),
    gettext_domain='checkbox-provider-vienna',)
