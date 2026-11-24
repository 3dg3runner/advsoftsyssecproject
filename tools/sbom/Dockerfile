FROM python:3.12-slim@sha256:191083cdf6c7bda8c76158983163ead5d5cf7b77cf3033e805bb0f5296f51b4b

ARG SYFT_VERSION=1.57.2
ARG TRIVY_VERSION=0.76.2
ARG CYCLONEDX_BOM_VERSION=9.0.0

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSfL https://raw.githubusercontent.com/anchore/syft/v${SYFT_VERSION}/install.sh \
      | sh -s -- -b /usr/local/bin v${SYFT_VERSION}
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/v${TRIVY_VERSION}/contrib/install.sh \
      | sh -s -- -b /usr/local/bin v${TRIVY_VERSION}

RUN python -m venv /opt/tools \
    && /opt/tools/bin/pip install "cyclonedx-bom==${CYCLONEDX_BOM_VERSION}"
ENV PATH="/opt/tools/bin:${PATH}"

WORKDIR /work
